import sys
import os
#import fileinput

"""

CLASSES: 
	- Scanner: moves through the file, maintaining a dictionary of line numbers and lines where the word appears
"""

class Scanner:
	"""
	ATTRIBUTES:
		- search_term: specified by the user
		- hits: dictionary of lines and line number (key)

	METHODS:
		- naive_traversal: provides a method for moving through a file linearly and 
			peforming an action at each step
		- hit_check: checks any block of text for exact matches to search term
		- get_results: prints the results in readable terms

	 """

	def __init__(self,search_term):
		"""Create an instance of a scanner with an empty list of hits"""
		self.search_term = search_term
		self.hits = {}

	def naive_traversal(self,fn,file_name = None):
		"""Traverse a file, performing fn on each line"""
		line_number = 1
		with open(file_name,'r') as f:
			for line in f:
				fn(text=line,position=line_number,search_term= self.search_term)
				line_number +=1

	def hit_check(self,text=None,search_term=None,position=None):
		"""Check text for search_term in each line & store matches"""
		words = text.split()
		if search_term in words:
			self.hits[position] = text.rstrip('\n')

	def get_results(self):
		"""Print the search results"""
		print "\r\n----Results----"

		if self.hits:
			total_hits = len(self.hits)
			print "Search term: %s"%self.search_term
			print "\r\nTotal hits: %s"%total_hits
			
			for key, value in self.hits.items():
				print "    Line {0}: '{1}'".format(key,value)
		else: 
			print " '%s' does not appear in the document" %search_term




# class InvertedIndexer:

# 	def __init__(self):
# 		self.index = {}	

# 	def add_to_index():
# 		"""Adds a """

if __name__ == '__main__':
	try: 
		file_name = sys.argv[1]
	except IndexError: 
		print "Please enter a filename."
	if os.path.exists(file_name):
		search_term = raw_input("Search term:")
		s = Scanner(search_term)
		s.naive_traversal(s.hit_check, file_name = file_name)
		s.get_results()
	else:
		print "Please enter a valid filename"
