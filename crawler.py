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
	def __init__(self,start = 'http://www.nytimes.com',depth = default_depth):
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
		data = urllib2.urlopen(url).read()
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
 - Add support for parent layers"""




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


