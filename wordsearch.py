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


		# line_number = 0
		# current_line = ''
		# while current_line:
		# 	hit_checker.line_check(current_line)
		# 	line_number+++

	def get_results(self):
		"""Print hits or empty string"""
		print "Your results are:"
		if hit_tracker.hits:
			total_hits = len(hit_tracker.hits)
			print "You have %s hits:/n"%total_hits
			for key, value in hit_tracker.hits.items():
				print key, value
		else: 
			print " '%s' does not appear in the document" %search_term


class HitTracker:

	def __init__(self):
		self.hits = {}

	def line_check(self,string,search_term,line_number):
		"""Takes in a string, adds it to the list of hits """
		words = string.split()
		# print words
		if search_term in words:
			self.hits[line_number] = string
			print 'The word was present'






if __name__ == '__main__':
	try: 
		file_name = sys.argv[1]
	except IndexError: 
		print "Please retry with a valid filename."
	else:
		search_term = raw_input("Search term:")
		s = Scanner(file_name,search_term)
		s.traverse_file()
		s.get_results

