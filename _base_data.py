import math

import numpy as np
import yfinance as yf 

data = yf.download("AAPL", start="2017-01-01", end="2022-06-30")