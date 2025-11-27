import sys
from pykrx import stock



value = sys.argv[1]  

df = stock.get_market_ohlcv_by_date(fromdate="20200101", todate="20241231", ticker="005930")
print(df)

