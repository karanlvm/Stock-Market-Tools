import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

# Defining the time frame

start = dt.datetime(2021,1,1)
end = dt.datetime.now()

# Load the data

data = web.DataReader('GS', 'yahoo', start, end)

# Data Formatting

data = data[['Open', 'High', 'Low', 'Close']]

data.reset_index(inplace=True)
data['Date'] = data['Date'].map(mdates.date2num)

print(data.head())

# Plotting the data

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('Share Price', color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=0.5, colorup='#00ff00')
plt.show()
