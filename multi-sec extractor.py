from datetime import datetime

import yfinance as yf
import pandas as pd

# setting time frame
start_date = datetime(year=2010 , month=1, day=1) # insert preferred date
end_date = datetime(year=2021 , month=1 , day=1)  # insert preferred date

# setting tickers
tickers = ("ticker1" , "ticker2", "ticker3",
        ) # change tickers for preferred securities, don't download too much data at once, be nice :)

# shaping the data
(
    yf.download(
        tickers=tickers,
        start = start_date,
        end = end_date,
        interval = "1mo", # available common intervals 1d 1wk 1mo 1y
        auto_adjust = False,
        group_by = "ticker",
        progress = False
    )
.to_excel("name.xlsx", index = True ) # change .xlsx for preferred name
)

