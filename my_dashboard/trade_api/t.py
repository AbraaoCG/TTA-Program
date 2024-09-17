from b3_api import get_last_records

[ticker, num_records, minutes_interval] = 'PETR4.SA', 5, 5
r = get_last_records(ticker, num_records, minutes_interval)
r2 = r.iloc[-1]
print(r2, r.index[-1])