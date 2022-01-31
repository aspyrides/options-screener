from yahoo_fin import options
import pandas as pd


class OptionData:
    def __init__(self, ticker, c_or_p=None):
        self.ticker = ticker
        self.c_or_p = c_or_p
        self.calls = None
        self.puts = None
        self.expiration_dates = None
        self.get_data()

    def get_data(self):
        # Get Expiration Dates
        self.expiration_dates = options.get_expiration_dates(self.ticker)

        # Get Call and Put data
        if (self.c_or_p == 'c'):
            self.calls = options.get_calls(self.ticker)
        elif (self.c_or_p == 'p'):
            self.puts = options.get_puts(self.ticker)
        else:
            self.calls = options.get_options_chain(self.ticker)['calls']
            self.puts = options.get_options_chain(self.ticker)['puts']

        self.prepare_data()

    def prepare_data(self):
        # Get Expiry Date in its own column
        if (self.calls is not None):
            self.calls["Expiry Date"] = pd.to_datetime(
                self.calls["Contract Name"].str[len(
                    self.ticker):(len(self.ticker)+6)],
                format='%y%m%d')
        if (self.puts is not None):
            self.puts["Expiry Date"] = pd.to_datetime(
                self.puts["Contract Name"].str[len(
                    self.ticker):(len(self.ticker)+6)],
                format='%y%m%d')


c1 = OptionData('aapl')

c1.calls
