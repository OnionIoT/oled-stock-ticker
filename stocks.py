import sys
import json
import urllib3
import re

# character lengths for formatting
L_LINE = 21     # when using oledExp.setTextColumns
L_NAME = 4      # max 4 characters
L_PRICE = 8     # allow up to 9999.99
L_CHANGEP = 6   # max 99.99% (not including +/- sign, but including % sign)

def readJsonFile(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data
    
# sends request to google finance api, receives json array with some characters in front
# turn response into python object
def readGoogleFinance(response):
    data = response.replace("\n","")            # remove newlines
    data = re.sub(r'^// ', '', data)    # remove padding characters at beginning    
    data = json.loads(data)                 # read the json
    return data                             # returns a list of dicts 

# get a list of stock info objects from api    
def getStocks(stocks):
    http = urllib3.PoolManager()
    url = "http://www.google.com/finance/info?q="
    for i in range(0, len(stocks)):
        url += stocks[i] + ","                    # add stock tickers to request
    
    stocksRequest = http.request('GET', url)      # send request
    return readGoogleFinance(stocksRequest.data.decode('utf-8'))             # returns list of stock objects

# formats the data returned from google api into a neat string
# adjust to what you want to see
def formatGoogleStockInfo(googleStock):
    stockInfo = {                                      # append some of the fields to a dictionary for easier access
        "ticker": googleStock["t"],
        "price": googleStock["l_fix"],
        "change": googleStock["c_fix"],
        "changeDirection": "+" if float(googleStock["c_fix"]) >= 0 else "-",
        "changePercentageAmount": str(abs(float(googleStock["cp_fix"])))
    }
    stockString = stockInfo["ticker"].ljust(L_NAME)
    stockString += " "
    formattedPrice = "$" + stockInfo["price"]
    stockString += formattedPrice.rjust(L_PRICE)
    stockString += " " + stockInfo["changeDirection"]
    formattedChangePercentage = stockInfo["changePercentageAmount"] + "%"
    stockString += formattedChangePercentage.rjust(L_CHANGEP)
    
    return stockString

if __name__ == '__main__':
    print json.dumps(getStocks([sys.argv[1]]), indent=4)
    