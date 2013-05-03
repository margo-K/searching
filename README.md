#Search Engine

### **rlink**: a formula for relevance
A separate rlink value is calculated for each word on each page

**Pterm** = prominence of the term on the page (True <=> word occurs in keywords metatag or one of the headers)
**Rterm** = number of occurences of the term on the page (in any position)
> Output:
***rlink(page,term) = Rterm/(Total words on the page) + Pterm**

Note: 'total words on the page' = sum(word*number of occureces of word) for all non-useless words on the page
###Contents:
Each of the following can be run independently:
- __test_search.py__ 
- crawler.py:
- indexer.py:
*automatically indexes http:://www.nytimes.com and pretty prints the inverse index created from this page
*output is a list of tuples of the form ('word_from_text',rlink value)

Required for querying but never called alone:
- query.py: query1 is used for terminal version, query2 is used for browser version



###Requirements
- mongodb
- pymongo
- lxml
- beautifulsoup4

###Getting Started
####Command Line Version
#####Open REPL

To start the crawler:
```
python crawler.py [optional urls, separated by commas] [optional depth]

``` 

To query the current index: 
From the command line:
```
python test_search.py

```
>>>Insert Demo<<< (with 'Please enter a search term:')

####Browser Version

#####Additional Contents
- searchapp.py
- templates/index.html

#####Requirements
- flask

###To do:
* add multi-word search, phrase searching, case sensitivity options (with and without possible words in between)
* add indexing method into WordSearch so that traversal can either check for matches or create an index
* add an HTML parser to the htmlgrab and integrate with the indexer to allow for better searching
* build out actual class structure in the htmlgrabber
* related word searching
* And lots more!



