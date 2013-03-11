from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin
import pprint
import time
import string
# DEFAULT_URLS = ['http://www.google.com','http://www.amazon.com','http://www.nytimes.com','http://www.racialicious.com','http://www.groupon.com','http://www.yelp.com']

USELESS_WORDS = ['a','an','the','in','from','to','at','on']+range(10)+list(string.letters)+list(string.punctuation)

def is_meta_keyword_tag(tag):
	return tag.has_key('name') and tag['name']=='keywords'

def parse_line(unicode_text):
		"""Return a list of ascii-charactered words"""
		return [word.strip(string.punctuation) for word in unicode_text.encode('ascii','ignore').split()]

def rlink(frequency,total_terms,prominent):
		"Return the rlink(a relevancy metric) of a function"
		return float(frequency)/total_terms + prominent

class Page(BeautifulSoup):

	def __init__(self,url):
		self.url = url
		try:
			data = urllib2.urlopen(url).read()
		except urllib2.HTTPError:
			raise IndexerError
		else:
			super(Page,self).__init__(data)
			self.links = self._get_clickable_links()
			self.paragraph_text = self._get_paragraph_text()
			self.header_text = self._get_header_text()
			self.keywords = self._get_keywords()
			self.crawl_time = time.time()
			self.index = {} 
			self._make_index(self.header_text+self.keywords,prominent=True)
			self._make_index(self.paragraph_text)

	def _get_clickable_links(self):
		links = []
		for link in self.find_all('a'):
			formatted_link = urljoin(self.url,link.get('href'))
			if formatted_link.startswith('http'):
				links.append(formatted_link)
		return links

	def _get_paragraph_text(self):
		return [p.get_text().strip() for p in self.find_all('p')]

	def _get_header_text(self):
		headers = ['h1','h2','h3','h4','h5','h6']
		return [h.get_text().strip() for h in self.find_all(headers)]

	def _get_keywords(self):
		keywords = []
		tag = self.find(is_meta_keyword_tag)
		if tag:
			try:
				keywords+= tag.attrs['content'].split(",")
			except KeyError:
				"Print keyword but no contents"
		return keywords

	def _make_index(self,page_text,prominent=False):
		"""Add words in page_text to the page's index"""
		for line in page_text:
			working_list = [elem.lower() for elem in parse_line(line) if elem  and elem not in USELESS_WORDS]
			for item in working_list:
				if item and item not in self.index:
					# self.index[item] = {'url': self.url, 'prominent': prominent, 'count': 1}
					self.index[item] = {'prominent': prominent, 'count': 1}
				else:
					self.index[item]['prominent'] = prominent or self.index[item]['prominent']	
					self.index[item]['count'] += 1

	def make_record(self):
		fields = ['url','crawl_time','paragraph_text','header_text','keywords']
		return {key: self.__dict__[key] for key in fields}

	def make_rlink_index(self):
		"""Return list of tuples of the form (word, rlink)"""
		total_terms = len(self.index.keys())
		output = []

		for word in self.index:
			frequency = self.index[word]['count']
			prominence = self.index[word]['prominent']
			relevance_score = rlink(frequency,total_terms,prominence)
			output.append((word,relevance_score))
		return output


class IndexerError(Exception):
	def __init__(self):
		pass
	def __str__(self):
		return "The link could not be opened"	

if __name__ == '__main__':
 	url = 'http://www.nytimes.com'
 	p = Page(url)
 	# print p.make_record()
 	# pprint.pprint(p.index)
 	pprint.pprint(p.make_rlink_index())


