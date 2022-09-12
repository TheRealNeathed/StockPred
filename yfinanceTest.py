import pandas as pd
from datetime import datetime as dt
import urllib.request
import json
import plotly.express as px
import yfinance as yf

tickerList = ["MSFT", "GOOGL", "AAPL"]
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
    timeList = Formatdata_2["timestamp"].tolist()
    tempEsgList = Formatdata_2["esgScore"].tolist()
    #print(tempTimeList[63]
    i = 0
    while i <= 62:
        tempEsgList[i] = 100 - tempEsgList[i]
        i += 1
    esgList.append(tempEsgList)
fig = px.scatter(x=timeList, y=esgList)
fig.update_yaxes(range=[0, 100])
fig.show()


