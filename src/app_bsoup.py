import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
# Select the resource to download
#resource_url = "https://quotes.toscrape.com/"
resource_url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
#response = requests.get(resource_url,timeout=10)
response = requests.get(resource_url, headers = headers,timeout=10)
# Request to download the file from the Internet
debug = ""
# If the request was executed correctly (code 200), then the file could be downloaded
df = pd.DataFrame(columns=['Date','Revenue'])
if response:
    page_html=response.text
    #print(response.text)
    # The file is stored in the current directory for later use
    #with open("adult.csv", "wb") as dataset:
    #    dataset.write(response.content)
    page_bs4=BeautifulSoup(page_html)

    for tag_div in page_bs4.find_all(class_="historical_data_table"):
        if tag_div.find_all( string = re.compile("Tesla Quarterly Revenue")):
        #for tag_a in tag_div.find_all("a", class_="tag"):
#Parte 3
            print("_______________________")
            #print(tag_div.text)
            # Collecting Ddata
            for row in tag_div.tbody.find_all('tr'):   
                # Find all data for each column
                columns = row.find_all('td')
                if(columns != []):
                    date = columns[0].text.strip()
                    #parte 4
                    revenue =re.sub(r'[$,]', '', str(columns[1].text.strip()))
                    #print(date,revenue)
                    aux = pd.DataFrame([[date,revenue]],columns=['Date','Revenue'])
                    df = pd.concat([df,aux], ignore_index=True)

else: 
    print("not working")

print(df.head())
#Parte 5
import sqlite3

connection = sqlite3.connect("Tesla.db")
print(connection)
cursor = connection.cursor()
#cursor.execute("""CREATE TABLE revenue (Date, Revenue)""")
tesla_tuples = list(df.to_records(index = False))
print(tesla_tuples[:5])
#cursor.executemany("INSERT INTO revenue VALUES (?,?)", tesla_tuples)
connection.commit()

for row in cursor.execute("SELECT * FROM revenue"):
    print(row)
    
#Parte 6

import matplotlib.pyplot as plt
import seaborn as sns

# Convert non-numeric values in "Revenue" column to NaN
df["Revenue"] = pd.to_numeric(df["Revenue"], errors='coerce')

# Drop rows with NaN values in "Revenue" column
df.dropna(subset=["Revenue"], inplace=True)

# Convert "Revenue" column to integer type
df["Revenue"] = df["Revenue"].astype(int)

# Plotting
fig, axis = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df, x="Date", y="Revenue")
plt.tight_layout()
plt.show()