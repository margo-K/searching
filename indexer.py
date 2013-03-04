from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin
import pprint
import time
# DEFAULT_URLS = ['http://www.google.com','http://www.amazon.com','http://www.nytimes.com','http://www.racialicious.com','http://www.groupon.com','http://www.yelp.com']

def is_meta_keyword_tag(tag):
	return tag.has_key('name') and tag['name']=='keywords'

class Page(BeautifulSoup):

	def __init__(self,url):
		self.url = url
		try:
			data = urllib2.urlopen(url).read()
		except urllib2.HTTPError:
			raise IndexerError
		else:
			super(Page,self).__init__(data)
			self.links = self.get_clickable_links()
			self.header_text = self.get_paragraph_text()
			self.keywords = self.get_header_text()
			self.paragraph_text = self.get_keywords()
			self.crawl_time = time.time()

	def get_clickable_links(self):
		links = []
		for link in self.find_all('a'):
			formatted_link = urljoin(self.url,link.get('href'))
			if formatted_link.startswith('http'):
				links.append(formatted_link)
		return links

	def get_paragraph_text(self):
		return [p.get_text().strip() for p in self.find_all('p')]

	def get_header_text(self):
		headers = ['h1','h2','h3','h4','h5','h6']
		return [h.get_text().strip() for h in self.find_all(headers)]

	def get_keywords(self):
		return self.find(is_meta_keyword_tag).attrs['content'].split(",")

	def make_record(self):
		fields = ['url','crawl_time','paragraph_text','header_text','keywords']
		return {key: self.__dict__[key] for key in fields}

class IndexerError(Exception):
	def __init__(self):
		pass
	def __str__(self):
		return "The link could not be opened"	

if __name__ == '__main__':
 	url = 'http://ww.nytimes.com'
 	p = Page(url)
 	print p.make_record()


