import alpha_vantage
from alpha_vantage.timeseries import TimeSeries

class PortfolioTracker:
    def __init__(self, api_key):
        self.api_key = api_key
        self.ts = TimeSeries(key=self.api_key)
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            print("Stock already exists in portfolio.")
            return
        else:
            self.portfolio[symbol] = {'shares': shares, 'cost_basis': None}

    def remove_stock(self, symbol):
        if symbol in self.portfolio:
            del self.portfolio[symbol]
        else:
            print("Stock not found in portfolio.")

    def update_portfolio(self):
        for symbol in self.portfolio.keys():
            data, _ = self.ts.get_quote_endpoint(symbol)
            if 'Global Quote' in data:
                latest_price = float(data['Global Quote']['05. price'])
                if self.portfolio[symbol]['cost_basis'] is None:
                    self.portfolio[symbol]['cost_basis'] = latest_price
                else:
                    self.portfolio[symbol]['cost_basis'] = latest_price * self.portfolio[symbol]['shares']

    def display_portfolio(self):
        print("Portfolio:")
        for symbol, details in self.portfolio.items():
            print(f"{symbol}: {details['shares']} shares")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key
    api_key = 'SAXGZ1GHFCWZ144H'
    tracker = PortfolioTracker(api_key)

    # Example usage:
    tracker.add_stock("AAPL", 10)
    tracker.add_stock("GOOGL", 5)

    tracker.display_portfolio()

    tracker.update_portfolio()

    tracker.display_portfolio()

