import json
import parse
import urllib


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
    
def getStocks(url, stocks):
    requestTarget = url
    for i in range(0, len(stocks)):
        requestTarget += stocks[x] + ","                    # add stock tickers to request
    site = urllib.urlopen(requestTarget)                    # send request
    rawResponse = site.read()                               # read response
    return parse.readGoogleFinance(rawResponse)             # returns list of stock objects