import requests
from bs4 import BeautifulSoup
import pandas as pd
import regex as re
import pprint

link = 'https://en.wikipedia.org/wiki/Comparison_of_digital_SLRs' 

def getAllRefs(url = str) :

    response = requests.get(url) #request which gets the url's encoded content
    soup = BeautifulSoup(response.text,'html.parser') #scrape Webpage. reponse.text : url's decoded content
    #print(soup.prettify()) # To see the html code of the Wikipedia page

    httpsrefs = {}

    # Get all the references in the body of the html code
    allrefs = soup.find(id="bodyContent").find_all(rel=True) #find all tags which have the attribute "rel"
    #print(allrefs)

    for ref in allrefs: 
        string = str(ref)
        element = "["
        if element in string :
            id = string[string.index(element) + 1]
        if ref['rel'] == ['nofollow'] : # We are only interested in https pages and not wiki articles
            if id not in httpsrefs :
                httpsrefs[id] = [ref.get('href')]
            else :
                httpsrefs[id].append(ref.get('href'))
        #try :
            #temp = re.search("(?P<url>https?://[^\s]+)", str(ref)).group("url")
            #httpsrefs[allrefs.index(ref)] = temp
        #except AttributeError :
            #pass
    #for key in list(httpsrefs) : #we deleted urls that are not in the table
        #if key > 129 :
            #httpsrefs.pop(key)
    pprint.pprint(httpsrefs)
    return(len(httpsrefs)) #length must be 130


def wikiTable_to_csv(url = str):
    tableName  = url.split("/")[-1]
    tables = pd.read_html(url, header=0) #reads html tables into a list of dataframe objects
    #print(tables)

    #If you want to test the code on linkBis, change the following "1"s by "0"s
    if not tables[1].empty:
        dataframeName = tableName + " table.csv"

        tables[1].to_csv(dataframeName, sep=',') 

intermediate = getAllRefs(link)
print(intermediate)
#result = wikiTable_to_csv(link)
#print(result)
