import sys
import Queue
import indexer
from pymongo import MongoClient,errors
import pprint
# import robotparser # used to check robot files

DEFAULT_URLS = ['http://www.google.com','http://www.amazon.com','http://www.nytimes.com','http://www.racialicious.com','http://www.groupon.com','http://www.yelp.com']
DEFAULT_DEPTH = 2

class BFS_Crawler:
	"""Create an instance of Crawler with a root and its tree"""
	def __init__(self,start = 'http://www.google.com',depth = DEFAULT_DEPTH):
		"""Initialize the crawler with the starting urls"""
		self.root = start
		self.depth = depth
		self.start = []
		try:
			self.simple_index = MongoClient().index_db.simple_index # mongo collection
		except errors.ConnectionFailure:
			print "Your attempt to connect failed"

	def process_page(self,url): 
		"""Retrieve all html data from a webpage,index it and return a list of links"""
		links = []
		try:
			page_object = indexer.Page(url)
		except indexer.IndexerError:
			print indexer.IndexerError
		else:
			return page_object

	def update_index(self,page):
		new_entries = page.make_rlink_index() # all new entries to be added to the db

		for entry in new_entries:
			term,rlink = entry
			url = page.url
			new_record = (url,rlink)

			self.simple_index.update({'_id':term},{'$push':{'pages':(url,rlink)}},upsert=True) # upsert will update or insert

		print "There are %s entries in the database"%str(self.simple_index.count())
		return True # returns only if no error is thrown

	def BFS_crawl(self):
		"""Return a sorted list of all links self.depth away from the original"""

		nodes = Queue.Queue()
		nodes.put((self.root,0))#enqueues (start,layer)
		ever_seen = set()
		ever_crawled = set()

		ever_seen.add(self.root)
		current_depth = 0

		while not (nodes.empty() or current_depth > self.depth):
			current_url, current_depth = nodes.get()

			print "This is the current node and its current depth"
			print current_url, current_depth
			
			page = self.process_page(current_url) # # index the page, (maybe in try-catch)
			if page:
				if self.update_index(page):
					ever_crawled.add(current_url)# record-keeping

					for link in page.links:
						if link not in ever_seen:
							nodes.put((link,current_depth+1)) # put it in the queue to be crawled
							ever_seen.add(link)
				else:
					ever_seen.remove(current_url)

		print "You've done it"
						

if __name__ == '__main__':
	c = BFS_Crawler()
	c.BFS_crawl()
	



