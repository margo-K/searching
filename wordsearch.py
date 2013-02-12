#Arguments: text file to be searched
#I/O: requests a search term
#Output: <True> Line Number and full line, if present; 
#Else, prints "The term <term> does not appear in the document"

# from stringplus import *
import sys
"""
CLASSES: 
	- Scanner: moves through the file, maintaining a hit list
	- MatchChecker: checks whether a match is found in an input sequence

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
		self.t = HitTracker()


	def traverse_file(self):
		"""Move through a file, from beginning to end, checking for hits"""
		
		line_number = 1
		for line in self.file:
			self.t.line_check(line,self.search_term,line_number)
			line_number = line_number + 1

		#with open('filepathname', 'rb') as self.file:

	def get_results(self):
		"""Print hits or empty string"""
		print "\n----Results----"
		if self.t.hits:
			total_hits = len(self.t.hits)
			print "Search term: %s"%self.search_term
			print "Total hits: %s"%total_hits
			
			for key, value in self.t.hits.items():
				# print key, value
				print "    Line {0}: '{1}'".format(key,value)
		else: 
			print " '%s' does not appear in the document" %search_term


class HitTracker:

	def __init__(self):
		self.hits = {}

	def line_check(self,string,search_term,line_number):
		"""Takes in a string, adds it to the list of hits """
		words = string.split()
		if search_term in words:
			self.hits[line_number] = string.rstrip('\n')





if __name__ == '__main__':
	try: 
		file_name = sys.argv[1]
	except IndexError: 
		print "Please retry with a valid filename."
	else:
		search_term = raw_input("Search term:")
		s = Scanner(file_name,search_term)
		s.traverse_file()
		s.get_results()

