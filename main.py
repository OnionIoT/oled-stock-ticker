import stocks
import datetime
import oledDriver
config = stocks.readJsonFile('./config.json')

# setup constants and data structures
MAX_STOCKS = 7

# create a timestamp
now = datetime.datetime.now()
timeHeader = now.strftime("%Y-%m-%d : %X")

# prepare payload to write to screen
payload = [timeHeader]

# collect stock data
stockList = stocks.getStocks(config["stocks"])

for i in range(0, min(len(stockList), MAX_STOCKS)):
    stockString = stocks.formatGoogleStockInfo(stockList[i])
    payload.append(stockString)

oledDriver.writeLines(payload, 0)

