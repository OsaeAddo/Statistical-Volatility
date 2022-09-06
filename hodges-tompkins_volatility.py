from ._base_data import *


def hodges_tompkins(price_data, window=30, trading_periods=252, clean=True):
    log_return = (
        price_data["Close"] / price_data["Close"].shift(1).apply(np.log)
    )