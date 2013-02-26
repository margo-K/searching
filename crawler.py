import sys
import urllib2
from urlparse import urljoin
from bs4 import BeautifulSoup
import Queue
from bulbs.neo4jserver import Graph
# import robotparser # used to check robot files

DEFAULT_URLS = ['http://www.google.com','http://www.amazon.com','http://www.nytimes.com','http://www.racialicious.com','http://www.groupon.com','http://www.yelp.com']
DEFAULT_DEPTH = 2
DEFAULT_GRAPH = Graph()
DEFAULT_GRAPH = 'graph'

class BFS_Crawler:
	"""Create an instance of Crawler with a root and its tree"""
	def __init__(self,graph = DEFAULT_GRAPH,start = 'http://.com',depth = DEFAULT_DEPTH):
		"""Initialize the crawler with the starting urls"""
		self.g = graph
		self.root = start
		self.depth = depth
		self.visited = []
		self.start = []

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
		counter = 0
		nodes = Queue.Queue()
		# parent_depth = 0
		nodes.put((self.root,0))#enqueues (start,layer)
		self.g.vertices.create(url=self.root)
		# self.visited.append(self.root)
		current_depth = 0

		while not (nodes.empty() or current_depth > self.depth):
			current_node, current_depth = nodes.get()
			print "This is the current node and its current depth"
			print current_node, current_depth
			current_vertex = self.g.vertices.index.lookup(url=current_node).next()
			print "This is the current vertext"
			print current_vertex

			for link in self.extract_links(current_node): # Does not currently account for duplicate links
				try:
					link_vertex = self.g.vertices.index.lookup(url=link).next()
				except StopIteration: #when the vertex is not currently in the graph
					link_vertex = self.g.vertices.create(url=link)
				
				self.g.edges.create(current_vertex, "links to",link_vertex)

				if link in self.visited:
					pass
				else:
					self.visited.append(link)
					nodes.put((link,current_depth+1))
				print counter, link
				counter +=1


if __name__ == '__main__':
	# links = sys.argv[1] 
	# depth = sys.arv[2]
	g = Graph()
	c = BFS_Crawler(g)
	c.BFS_crawl()


"""
TO DO:
 - Add support for URL errors (like broken link)
 - Add an index"""


