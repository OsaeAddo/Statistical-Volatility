from ._base_data import *


def garman_klass(price_data, window=30, trading_periods=252, clean=True):
    log_hl = (price_data["High"] / price_data["Low"]).apply(np.log)
    log_co = (price_data["Close"] / price_data["Open"]).apply(np.log)