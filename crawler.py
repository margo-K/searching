import sys
import urllib2
from urlparse import urljoin
from bs4 import BeautifulSoup
import Queue
from bulbs.neo4jserver import Graph
import time
# import robotparser # used to check robot files

DEFAULT_URLS = ['http://www.google.com','http://www.amazon.com','http://www.nytimes.com','http://www.racialicious.com','http://www.groupon.com','http://www.yelp.com']
DEFAULT_DEPTH = 2
DEFAULT_GRAPH = Graph()

class BFS_Crawler:
	"""Create an instance of Crawler with a root and its tree"""
	def __init__(self,graph = DEFAULT_GRAPH,start = 'http://www.google.com',depth = DEFAULT_DEPTH):
		"""Initialize the crawler with the starting urls"""
		self.g = graph
		self.root = start
		self.depth = depth
		self.start = []

	def extract_links(self,url): 
		"""Retrieve all html data from a webpage and return a souped object"""
		links = []
		try:
			data = urllib2.urlopen(url).read()
		except urllib2.HTTPError as e:
			print "Could not open file: {}".format(e.errno,e.strerror)
		else:
			for link in BeautifulSoup(data).find_all('a'):
				formatted_link = urljoin(url,link.get('href'))
				if formatted_link.startswith('http'):
					links.append(formatted_link)
		return links

	def BFS_crawl(self):
		"""Return a list of all links self.depth away from the original"""

		nodes = Queue.Queue()
		nodes.put((self.root,0))#enqueues (start,layer)
		self.g.vertices.create(url=self.root)
		current_depth = 0

		while not (nodes.empty() or current_depth > self.depth):
			current_url, current_depth = nodes.get()
			current_vertex = self.g.vertices.index.lookup(url=current_url).next() #vertex object; lookup() returns a generator

			print "This is the current node and its current depth"
			print current_url, current_depth
			print "This is the current vertex:"
			print current_vertex

			for link in self.extract_links(current_url):
				# link_vertex = self.g.vertices.get_or_create('url',link)
				try:
					link_vertex = self.g.vertices.index.lookup(url=link).next()
				except AttributeError: #when the vertex is not currently in the graph
					link_vertex = self.g.vertices.create(url=link,crawled=time.time())
					nodes.put((link,current_depth+1))
				
				self.g.edges.create(current_vertex, "links to",link_vertex)

if __name__ == '__main__':
	# links = sys.argv[1] 
	# depth = sys.arv[2]
	g = Graph()
	c = BFS_Crawler(g)
	c.BFS_crawl()


"""
TO DO:
 - Add an index"""


