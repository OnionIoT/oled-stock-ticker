import json
import urllib

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
    data = response.replace("/", "")
    data = data.replace("\n","")
    data = json.loads(data)
    return data

# get a list of stock info objects from api    
def getStocks(stocks):
    requestTarget = "http://www.google.com/finance/info?q="
    for i in range(0, len(stocks)):
        requestTarget += stocks[i] + ","                    # add stock tickers to request
    site = urllib.urlopen(requestTarget)                    # send request
    rawResponse = site.read()                               # read response
    return readGoogleFinance(rawResponse)             # returns list of stock objects

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

def __main__():
    print "hello"
    print getStocks("http://www.google.com/finance/info?q=", ["AAPL"])

if __name__ == "__main__":
    __main__()