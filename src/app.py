import requests

# Select the resource to download
resource_url = "https://quotes.toscrape.com/"
#resource_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
#response = requests.get(resource_url,timeout=10)
response = requests.get(resource_url, headers = headers,timeout=10)
# Request to download the file from the Internet

# If the request was executed correctly (code 200), then the file could be downloaded
if response:
    print(response.text)
    # The file is stored in the current directory for later use
    #with open("adult.csv", "wb") as dataset:
    #    dataset.write(response.content)


    
else: 
    print("not working")

