import sys
import os


DEFAULT_FILE = '/Users/margoK/Dropbox/search/htmlgrab.py'
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

	def hit_check(self,text=None,search_term=None,position=None):
		"""Check text for search_term in each line & store matches"""
		
		words_to_search = text.split()

		for term in search_term:
			if term in words_to_search:
				self.hits[term].append((position,text.strip()))	

	def get_results(self):
		"""Print the search results"""
		print "\r\n------------Results--------------"

		for term in self.search_terms:
			print "Search term: %s"%term
			print "\r\nTotal hits: %s"%len(self.hits[term])
			if not self.hits[term]:
				print "\n '%s' does not appear in the document." %term
			else:
				for hit in self.hits[term]:
					line_number, line = hit
					print "\t\tLine {0}: '{1}'".format(line_number,line)


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
	s.get_results()
		




