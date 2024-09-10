import yfinance as yf

def get_current_prices(tickers):
    # Cria um dicionário para armazenar os preços
    prices = {}
    
    # Obtém os dados de cada ticker
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d')  # Obtém os dados do último dia
        if not data.empty:
            prices[ticker] = data['Close'].iloc[-1]  # Obtém o preço de fechamento mais recente

    return prices

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