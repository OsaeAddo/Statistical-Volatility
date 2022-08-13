# Parkinson's uses the asset's opening & closing prices rather than just the closing price
import math

import numpy as np
import yfinance as yf 

data = yf.download("AAPL", start="2017-01-01", end="2022-06-30")

def parkinson(price_data, window=30, trading_periods=252, clean=True):
    rs = (1.0 / (4.0 * math.log(2.0))) * (
        (price_data["High"] / price_data["Low"]).apply(np.log)
    ) ** 2
    
    def f(v):
        return (trading_periods * v.mean()) ** 0.5
    
    result = rs.rolling(window=window, center=False).apply(func=f)

    if clean:
        return result.dropna()
    else:
        return result
    
    
parkinson(data).plot()