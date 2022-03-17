import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re

link = 'https://en.wikipedia.org/wiki/Comparison_of_digital_SLRs'
linkBis = 'https://en.wikipedia.org/wiki/List_of_most_visited_websites' 
response = requests.get(link) #request which gets the url's encoded content
soup = BeautifulSoup(response.text,'html.parser') #Scrape Webpage. reponse.text : url's decoded content
#print(soup.prettify()) # To see the html code of the Wikipedia page

#To create a text file temp in which one can save the html code of the Wikipedia page
#fichier = open("temp.txt", "w")
#fichier.write(soup.prettify())
#fichier.close()

def wikiTable_to_csv(url = str):
    httpsrefs = {}
    L =[]
    tableName  = url.split("/")[-1]
    tables = pd.read_html(url, header=0) #reads html tables into a list of dataframe objects
    #print(tables)

    #If you want to test the code on linkBis, change the following "1"s by "0"s
    if not tables[1].empty:
        dataframeName = tableName + " table.csv"

        # Get all the references in the body of the html code
        allrefs = soup.find(id="bodyContent").find_all("a")
        #print(allrefs)

        condition1 = "/wiki/"
        condition2 = "/w/"
        #condition3 = "#"
        for ref in allrefs: 
            if condition1 not in str(ref) and condition2 not in str(ref) : #and condition3 not in str(ref) : # We are only interested in https pages and not wiki articles
                httpsrefs[allrefs.index(ref)] = ref.get('href')
                #temp = re.search("(?P<url>https?://[^\s]+)", string).group("url")
                #httpsrefs[L.index(string)] = temp
        print(httpsrefs)
        print(len(httpsrefs)) #must be around 141
        tables[1].to_csv(dataframeName, sep=',') 

result = wikiTable_to_csv(link)
print(result)

#<a rel="nofollow" class="external text" href="https://www.optyczne.pl/895-Panasonic_Lumix_DMC-GH1-specyfikacja_aparatu.html">[1]</a>
