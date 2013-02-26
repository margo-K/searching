import urllib2
import os
import sys


DEFAULT_URLS = ['http://www.google.com','http://www.amazon.com','http://www.nytimes.com','http://www.racialicious.com','http://www.groupon.com','http://www.yelp.com']

current_directory = os.path.abspath(os.curdir)

class HTMLFiler:
	def __init__(self):
		self.created_files = []

	def html_grabber(self,urls = None):
		"""Grab all HTML from a page, write it to a new file in the specified directory (defaults to current directory)"""
		grabbed_info = []

		if urls is None:
			urls = DEFAULT_URLS

		for url in urls:
			site_name = url.split('www.')[1].rstrip('.com')
			try:
				filish_object = urllib2.urlopen(url)
			except urllib2.HTTPError as e:
				print "Could not open file: {}".format(e.errno,e.strerror)
			else:
				data = filish_object.read()
				grabbed_info.append((site_name, data))
		return grabbed_info
		

	def html_storer(self,info,directory = None):
		"""Store the data in a file """
		if directory is None:
			directory = current_directory
		for site_name,data in info:
			file_name = '{}/{}.html'.format(directory,site_name)

			new_file = open(file_name,'a')
			new_file.write(data)
			print "Site name: {} \n File: {}".format(site_name,file_name)
			new_file.close()

			self.created_files.append(file_name)

	def file_cleanup(self):
		"""Remove all files associated with this session of the filer
			Current: prints a list of all files created in this session"""
		print self.created_files


if __name__ == '__main__': 
	H = HTMLFiler()
	info_to_be_stored = H.html_grabber()
	H.html_storer(info_to_be_stored)


