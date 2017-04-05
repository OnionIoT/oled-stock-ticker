from config import config
import parse
import urllib

MAX_STOCKS = 7
stockInfo = []

for x in range (0, MAX_STOCKS):
    requestTarget = config["url"] + config["stocks"][x]
    site = urllib.urlopen(requestTarget)
    rawResponse = site.read()

    financeObject = parse.readGoogleFinance(rawResponse)
    stockInfo.append({
        "ticker": financeObject["t"],
        "price": financeObject["l_fix"]
    })

print stockInfo