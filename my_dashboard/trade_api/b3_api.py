import yfinance as yf

def get_current_price(ticker, num_records, minutes_interval):
    stock = yf.Ticker(ticker)
    data = stock.history(period=f'1d', interval=f'{minutes_interval}m')
    
    return [data['Close'].iloc[-1],data.index[-1]]

def get_last_records(ticker, num_records, minutes_interval):
    stock = yf.Ticker(ticker)
    data = stock.history(period=f'1d', interval=f'{minutes_interval}m')
    if len(data) >= num_records:
        return data['Close'].tail(num_records)
    else:
        return data['Close']

# stock = yf.Ticker("ABEV3.SA")
# price = stock.info['regularMarketPrice']
# print(price)