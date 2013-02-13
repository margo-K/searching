import urllib2
import os
import pdb

def html_grabber(*urls):
	# # pdb.set_trace()
	for url in urls:
		site_name = url.split('www.')[1].rstrip('.com')
		print "This is the name of the site: %s" %(site_name)
		new_file = open('/Users/margoK/Dropbox/search/%s.html'%site_name,'a') 
		file_handle = urllib2.urlopen(url)
		data = file_handle.read()
		print "Current path is: %s" %(os.path.abspath(os.curdir))
		new_file.write(data)
		new_file.close()

if __name__ == '__main__':
	urls = ['http://www.google.com','http://www.amazon.com','http://www.nytimes.com']
	html_grabber(urls[0],urls[1],urls[2])