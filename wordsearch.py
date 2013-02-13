import sys
import os

"""
CLASSES: 
	- Scanner: moves through the file, maintaining a dictionary of line numbers and lines where the word appears
"""

class Scanner:
	"""
	ATTRIBUTES:
		- hits: a list of all line numbers and lines in which they appear

	METHODS: 
	 """

	def __init__(self,file_name,search_term):
		"""Create an instance of a scanner with an empty list of hits"""
		self.search_term = search_term
		self.file = open(file_name,'rb') #opens the file in binary mode
		self.hits = {}


	def naive_traversal(self,fn):
		"""Move through a file line by line, performing whatever function is in the argument"""
		
		line_number = 1
		for line in self.file:
			# self.t.fn(*args)
			fn(line=line,line_number=line_number,search_term = self.search_term)
			line_number = line_number + 1

		#with open('filepathname', 'rb') as self.file:

	def get_results(self):
		"""Print hits or empty string"""
		print "\n----Results----"

		if self.hits:
			total_hits = len(self.hits)
			print "Search term: %s"%self.search_term
			print "Total hits: %s"%total_hits
			
			for key, value in self.hits.items():
				print "    Line {0}: '{1}'".format(key,value)# print key, value
		else: 
			print " '%s' does not appear in the document" %search_term

	def line_check(self,line=None,search_term=None,line_number=None):
		"""Takes in a string, adds it to the list of hits """
		words = line.split()
		if search_term in words:
			self.hits[line_number] = line.rstrip('\n')


class InverseIndex:

	def __init__(self):
		self.index = {}	

	def add_to_index():
		"""Adds a """

if __name__ == '__main__':
	try: 
		file_name = sys.argv[1]
	except IndexError: 
		print "Please enter a filename."
	if os.path.exists(file_name):
		search_term = raw_input("Search term:")
		s = Scanner(file_name,search_term)
		s.naive_traversal(s.line_check)
		s.get_results()
	else:
		print "Please enter a valid filename"
