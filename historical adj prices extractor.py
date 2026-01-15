# import the necessary packages
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import pandas as pd
from pandas.core.groupby.base import groupby_other_methods

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# set the start and end dates for our market data request
end_date = datetime(year=2026, month=1, day=30)
start_date = datetime(year=2010, month=5, day=21)
# set the name of the ticker we want to download market data for
ticker = (" "
          )

# download market data and process it in a single chained operation
(
    yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        interval="1d",
        group_by="ticker",
        auto_adjust=False,
        progress=False
    )
    # Rinomina esplicitamente le colonne per appiattire l'indice
    .pipe(lambda df: df.set_axis(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1))
    # Seleziona solo la colonna desiderata 'Adj Close'
    [['Adj Close']]
    # Export to Excel
    .to_excel("file name.xlsx", sheet_name="Adj Close", index=True)
)








