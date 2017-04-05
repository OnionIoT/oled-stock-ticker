from config import config
import parse
import urllib
import datetime
import oledDriver

# setup constants and data structures
MAX_STOCKS = 7

# create a timestamp
now = datetime.datetime.now()
timeHeader = now.strftime("%Y-%m-%d : %X")

# prepare payload to write to screen
payload = [timeHeader]

# collect stock data
for x in range (0, min(len(config["stocks"]), MAX_STOCKS)):
    requestTarget = config["url"] + config["stocks"][x]     # build url with query string
    site = urllib.urlopen(requestTarget)                    # send request
    rawResponse = site.read()                               # read response
    financeObject = parse.readGoogleFinance(rawResponse)    # parse the google finance object
    
    stockInfo = {                                      # append some of the fields to a list
        "ticker": financeObject["t"],
        "price": financeObject["l_fix"]
    }
    stockString = stockInfo["ticker"] + ": " + stockInfo["price"]
    
    payload.append(stockString)

oledDriver.writeLines(payload, 0)

