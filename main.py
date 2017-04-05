import datetime
import oledDriver
config = parse.readJsonFile('./config.json')

# setup constants and data structures
MAX_STOCKS = 7

# character lengths for formatting
L_LINE = 21     # when using oledExp.setTextColumns
L_NAME = 4      # max 4 characters
L_PRICE = 6     # allow up to 999.99
L_CHANGEP = 4   # max +/- 99.99 %


# create a timestamp
now = datetime.datetime.now()
timeHeader = now.strftime("%Y-%m-%d : %X")

# prepare payload to write to screen
payload = [timeHeader]

# collect stock data
stocks = stocks.getStocks(config["url"], config["stocks"])

for i in range(0, min(len(stocks), MAX_STOCKS)):
    stockInfo = {                                      # append some of the fields to a list
        "ticker": stocks[i]["t"],
        "price": stocks[i]["l_fix"]
    }
    stockString = stockInfo["ticker"].ljust(L_NAME) + ": $" + stockInfo["price"].ljust(L_PRICE) + " "
    
    payload.append(stockString)

oledDriver.writeLines(payload, 0)

