import json

def readJsonFile(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data
    
# turn the google finance api response into python object
def readGoogleFinance(response):
    data = response.replace("/", "")
    data = data.replace("\n","")
    data = data.replace("[","")
    data = data.replace("]","")
    data = json.loads(data)
    return data