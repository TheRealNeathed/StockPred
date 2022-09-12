import pandas as pd
from datetime import datetime as dt
import urllib.request
import json
import plotly.express as px
x = 0
dataframes = []
tickerList = ["MSFT", "GOOGL", "A", "AAPL"]
timeList = []
esgList = []
for ticker in tickerList:
    url = "https://query2.finance.yahoo.com/v1/finance/esgChart?symbol=" + str(ticker)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    data_2 = json.loads(data)
    Formatdata = data_2["esgChart"]["result"][0]["symbolSeries"]
    Formatdata_2 = pd.DataFrame(Formatdata)
    Formatdata_2["timestamp"] = pd.to_datetime(Formatdata_2["timestamp"], unit="s")
    tempTimeList = Formatdata_2["timestamp"].tolist()
    tempESGList = Formatdata_2["esgScore"].tolist()
    esgList.append(tempESGList)
    #print(Formatdata_2.head())
    for i in Formatdata_2["timestamp"]:
        print(i.type())
print(esgList) 
print(tempTimeList)

fig = px.scatter(x = tempTimeList,y = esgList)
fig.show()
