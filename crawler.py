import sys
import urllib2
from urlparse import urljoin
# from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import Queue
#Example link:<a href="http://www.w3schools.com/">Visit W3Schools</a>
#Global - href="http://www.cnn.com/" Links to other domains outside your website domain.
# Local - href="../internal/mypage2.html"   Links to other pages within your website domain.
# Internal - href="#anchorname" Links to anchors embedded in the current web page.
# E-mail Link: <a href="mailto:email@tizag.com?subject=Feedback&body=Sweet site!">Email@tizag.com</a>
# Download Link: <a href="http://www.tizag.com/pics/htmlT/blanktext.zip">Text Document</a>


default_urls = ['http://www.google.com','http://www.amazon.com','http://www.nytimes.com','http://www.racialicious.com','http://www.groupon.com','http://www.yelp.com']
default_depth = 2

class BFS_Crawler:
	"""Create an instance of Crawler with a root and its tree"""
	def __init__(self,start = 'http://www.racialicious.com',depth = default_depth):
		"""Initialize the crawler with the starting urls"""
		self.root = start
		self.depth = depth
		layer_map = {}
		# self.start = []
		# for url in start:
		# 	self.start.append(url)

	def extract_links(self,url): # note: all of the links have a u''
		"""Retrieve all html data from a webpage and return a souped object"""
		links = []
		try:
			data = urllib2.urlopen(url).read()
		except urllib2.HTTPError as e:
			print "Could not open file: {}".format(e.errno,e.strerror)
		else:
			for link in BeautifulSoup(data).find_all('a'):
				links.append(urljoin(url,link.get('href')))
		return links

	def BFS_crawl(self):
		"""Return a list of all links self.depth away from the original"""
		# depth = 0
		nodes = Queue.Queue()
		# parent_depth = 0
		nodes.put(self.root)#enqueues the start item in the queue

		while not nodes.empty():
			current_node = nodes.get()
			for link in self.extract_links(current_node): # Does not currently account for duplicate links
				nodes.put(link)
				print link



# class Link_Tree:
# 	"""Provides a basic data structure for link relations"""


# class LinkParser(HTMLParser):
# 	"""Handles functions dealing with HTML Parsing"""

# 	def handle_date()






if __name__ == '__main__':
	# links = sys.argv[1] 
	# depth = sys.arv[2]

	c = BFS_Crawler()
	c.BFS_crawl()


"""
TO DO:
 - Add support for URL errors (like forbidden or broken link)
 - Add support for parent layers
 - Add an index, so each page """

 # HTMLParser.HTMLParseError: malformed start tag, at line 1746, column 132

# /Library/Python/2.7/site-packages/bs4/builder/_htmlparser.py:149: RuntimeWarning: Python's built-in HTMLParser cannot parse the given document. This is not a bug in Beautiful Soup. The best solution is to install an external parser (lxml or html5lib), and use Beautiful Soup with that parser. See http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser for help.
#   "Python's built-in HTMLParser cannot parse the given document. This is not a bug in Beautiful Soup. The best solution is to install an external parser (lxml or html5lib), and use Beautiful Soup with that parser. See http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser for help."))
# Traceback (most recent call last):
#   File "crawler.py", line 75, in <module>
#     c.BFS_crawl()
#   File "crawler.py", line 50, in BFS_crawl
#     for link in self.extract_links(current_node): # Does not currently account for duplicate links
#   File "crawler.py", line 37, in extract_links
#     for link in BeautifulSoup(data).find_all('a'):
#   File "/Library/Python/2.7/site-packages/bs4/__init__.py", line 172, in __init__
#     self._feed()
#   File "/Library/Python/2.7/site-packages/bs4/__init__.py", line 185, in _feed
#     self.builder.feed(self.markup)
#   File "/Library/Python/2.7/site-packages/bs4/builder/_htmlparser.py", line 150, in feed
#     raise e
# HTMLParser.HTMLParseError: bad end tag: u"</' + 'script>", at line 16, column 748
# [2]   Exit 127                opzn
# [4]   Done                    pos=Bar1
# [5]-  Done                    sn2=5b35bc29/49f095e7
# [8]+  Done                    ad=feb_hol_reg_bar1_hp_3J6LK_3J6L8
# Margos-MacBook-Air:search margoK$ 



# #All code drawns from http://answers.oreilly.com/topic/1088-how-to-build-a-simple-web-crawler/
# import urllib2
# from bs4 import BeautifulSoup
# from urlparse import urljoin #what does this do?
# import htmlgrab # maybe these files should be merged?

# # ignorewords = set(['the','of','to','and','a','in','is','it']) # what is this used for?

# html_doc = """
# <html><head><title>The Dormouse's story</title></head>

# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """

# ###################Drawn Verbatim from the info page ######################

# def crawl(self,pages,depth=2): #Why this depth? what does depth refer to?
# 	for i in range(depth): # i in 1 or 2?
# 		newpages = set() # an empty set?
# 		for page in pages:
# 			try:
# 				c.urllib2.urlopen(page)
# 			except:
# 				print "Could not open %s" %page
# 				continue # is this necessary?

# 			soup = BeautifulSoup(c.read())
# 			self.addtoindex(page,soup)

# 			links = soup('a')
# 			for link in links:
# 				if ('href' in dict(link.attrs)):
# 					url = urljoin(page,link['href']) # what does urljoin do? A: make a valid urlstring
# 					if url.find("'")!=-1: continue #?
# 					url = url.split('#')[0] # remove location portion
# 					if url[]


