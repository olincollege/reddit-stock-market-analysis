import matplotlib.pyplot as plt
import pandas as pd
#import matplotlib
#import matplotlib.dates as mdates
#import datetime as dt
# df = pd.read_csv("stock_info/TSLAdata.csv")

# x = df['timestamp']
# print(x)
# y = df['close']
# print(y)


# x = [dt.datetime.strptime(str(val)[0:10],'%Y-%m-%d').date() for val in x]

x = [1,2,3,4]
y = [1,2,3,4]

plt.plot(x, y, ".")
#plt.show()