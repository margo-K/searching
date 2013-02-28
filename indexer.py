from bs4 import BeautifulSoup
import urllib2
DEFAULT_URLS = ['http://www.google.com','http://www.amazon.com','http://www.nytimes.com','http://www.racialicious.com','http://www.groupon.com','http://www.yelp.com']
# def database_init(file_path):
# 	"""Creates a new database"""


def is_meta_keyword_tag(tag):
	return tag.has_key('name') and tag['name']=='keywords'

class Indexer:

	def index(self,urls=DEFAULT_URLS):
		for url in urls:
			soup = BeautifulSoup(urllib2.urlopen(url).read())
			r = PageRecord(url)
			r.fill_record(soup)
			r.print_record()

				
class PageRecord:

	def __init__(self,url):
		self.url = url
		self.paragraph_text = []
		self.header_text = []
		self.keywords = []

	def _get_paragraph_text(self,soup):
		return [p.get_text() for p in soup.find_all('p')]

	def _get_header_text(self,soup):
		headers = ['h1','h2','h3','h4','h5','h6']
		return [h.get_text() for h in soup.find_all(headers)]

	def _get_keywords(self,soup):
		return soup.find(is_meta_keyword_tag).attrs['content'].split(",")

	def fill_record(self,soup):
		self.paragraph_text = self._get_paragraph_text(soup)
		self.header_text = self._get_header_text(soup)
		self.keywords = self._get_keywords(soup)

	def print_record(self):
		print "URL: {0}\r\n\nTEXT:\n\t{1}\r\n\nHEADERS:\n\t{2}\r\n\nKEYWORDS:\n\t{3}\r\n".format(self.url,self.paragraph_text,self.header_text,self.keywords)

	
if __name__ == '__main__':
	I = Indexer()
	sites = ['http://www.nytimes.com']
	I.index(sites)

