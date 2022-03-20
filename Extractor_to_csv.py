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
        string = str(ref)[-10:] # 'l">[1]</a>' for example
        condition = "["
        if condition in string :
            id = int(string[string.index("[") +1 :string.index("]")])
        if ref['rel'] == ['nofollow'] : # We are only interested in https pages and not wiki articles
            if id not in httpsrefs :
                httpsrefs[id] = [ref.get('href')]
            else :
                httpsrefs[id].append(ref.get('href'))
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
# #print(result)

#<a rel="nofollow" class="external text" href="https://www.optyczne.pl/895-Panasonic_Lumix_DMC-GH1-specyfikacja_aparatu.html">[1]</a>
