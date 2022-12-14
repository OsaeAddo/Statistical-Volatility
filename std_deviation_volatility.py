from ._base_data import *


def standard_deviation(price_data, window=30, trading_periods=252, clean=True):
    log_return = (price_data["Close"] / price_data["Close"].shift(1)).apply(np.log)
    result = log_return.rolling(window=window, center=False).std() * math.sqrt(trading_periods)

    if clean:
        return result.dropna()
    else:
        return result

standard_deviation(data).plot()