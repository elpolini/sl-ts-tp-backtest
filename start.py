import vectorbt as vbt
import numpy as np
import pandas as pd
import ccxt
import itertools
import ipywidgets
from datetime import datetime, timedelta
from numba import njit

seed = 42
symbols = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'BNBUSDT', 'ADAUSDT', 'LTCUSDT']
start_date = datetime(2020, 3, 24)
end_date = datetime(2023, 1, 19)
time_delta = end_date - start_date
window_len = timedelta(days=180)
window_count = 400
exit_types = ['SL', 'TS', 'TP', 'Random', 'Holding']
step = 0.01  # in %
stops = np.arange(step, 1 + step, step)

# vbt.settings.layout['template'] = vbt.settings.dark_template

vbt.settings.plotting["layout"]["template"] = "vbt_dark"
vbt.settings.portfolio['freq'] = '1d'
vbt.settings.portfolio['init_cash'] = 100.  # in $
vbt.settings.portfolio['fees'] = 0.0025  # in %
vbt.settings.portfolio['slippage'] = 0.0025  # in %
