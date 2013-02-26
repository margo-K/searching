import sys
import os


DEFAULT_FILE = 'htmlgrab.py'
DEFAULT_SEARCH_TERMS = ['the','if']

class Scanner:
	"""
	ATTRIBUTES:
		- search_term: specified by the user or default 
		- hits:
					hits = {
				 			word: [(line number, line), (line number, line)],
							word2: [(line number, line), (line number, line)]
							}

	METHODS:
		- naive_traversal: provides a method for moving through a file linearly and 
			peforming an action at each step
		- hit_check: checks any block of text for exact matches to search term
		- get_results: prints the results in readable terms

	 """

	def __init__(self,search_terms):
		"""Create an instance of a scanner with an empty list of hits"""
		self.search_terms = search_terms

	def naive_traversal(self,fn,file_name = None):
		"""Traverse a file, performing fn on each line"""
		self.hits = {}
		for term in self.search_terms:
			self.hits[term] = [] # Initiates hits as an empty list for each search term

		line_number = 1
		with open(file_name,'r') as f:
			for line in f:
				fn(text=line,position=line_number,search_term=self.search_terms)
				line_number +=1
		print self.hits

	def hit_check(self,text=None,search_term=None,position=None):
		"""Check text for search_term in each line & store matches"""
		
		words_to_search = text.split()

		for term in search_term:
			if term in words_to_search:
				self.hits[term].append((position,text))	

	def get_results(self):
		"""Print the search results"""
		print "\r\n------------Results--------------"

		if self.hits:
			total_hits = len(self.hits)
			print "Search term(s): %s"%self.search_terms
			print "\r\nTotal hits: %s"%total_hits
			
			for key, value in self.hits.items():
				print "\t\tLine {0}: '{1}'".format(key,value)
		else:
			for term in self.search_terms: 
				print "\n '%s' does not appear in the document." %term


if __name__ == '__main__':
	try: 
		file_name = sys.argv[1]
	except IndexError: # No user input, try with default
		file_name = DEFAULT_FILE
		search_terms = DEFAULT_SEARCH_TERMS
	else:
		if os.path.exists(file_name):
			response = raw_input("Search term(s):")
			search_terms = response.split(',') #returns an array
		else:
			file_name = DEFAULT_FILE
			search_terms = DEFAULT_SEARCH_TERMS
			print "No valid file name provided\nProceeding to search default file"

	s = Scanner(search_terms)
	s.naive_traversal(s.hit_check, file_name = file_name)
	# s.get_results()
		




