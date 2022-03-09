# Génie Logiciel Project

## Introduction

As part of our third and last year in engineering school at ENSAI we had to carry out a project in groups of 4 to 5 for the ***Génie logiciel*** course.
Thereof consisted in extracting tables from **Wikipedia** pages into the **CSV** format. <br>
It is not new that Wikipedia tables are difficult to exploit and analyse by spreadsheets and statistical tools due to the syntaxt they are written in : **Wikitext**. Not only this language was not designed for table specification but the heterogeneity in the way to write the tables also complicates even more the task. <br>
That is why our motivation here is to develop the most robust and general procedure to extract Wikipedia tables and to translate them in a simpler and more suitable format : the CSV one. <br>

A Wikipedia page can be analysed using two different methods : <br>
- By picking up the Wikitext code corresponding
- By exploiting the HTML rendering of the Wikipedia page 

In our case, we'll be choosing the second point. 

## The Python Extractor

The first basic extractor we constructed was in Python. It is mainly using packages such as *requests*, *BeautifulSoup4* and *pandas*. All of these dependencies can be installed by using the following command line from the root : <br>
``` $ pip3 install -r requirements.txt ``` <br>

Then one just has to execute the Python file such as : <br>
``` $ python3 ./Extractor_to_csv ``` <br>

Note that this extractor as only tested on one url which is [lien](https://en.wikipedia.org/wiki/Comparison_of_digital_SLRs) and may doesn't work for other.
