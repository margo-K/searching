#WordSearch 
This project is the beginning of a larger search engine project. Currently, the two files included in this repo just 
a) naively search specified files for a single search term 
b)generate HTML files from a few popular websites (i.e. something to be searched). 

Many more stages and a lot more functionality to come! 

###Contents
- __wordsearch.py__
- htmlgrab.py

###Getting Started
#####Open REPL

To search a file:
```
python wordsearch.py /path/to/file_being_searched

``` 

To generate HTML files to be searched (from 6 popular websites) and store them in the current directory: 

```
python html_grabber.py

```

###To do:
* add multi-word search, phrase searching, case sensitivity options (with and without possible words in between)
* add indexing method into WordSearch so that traversal can either check for matches or create an index
* add an HTML parser to the htmlgrab and integrate with the indexer to allow for better searching
* build out actual class structure in the htmlgrabber
* related word searching
* And lots more!