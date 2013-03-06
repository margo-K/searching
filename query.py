import pprint

def query(search_term,mongo_db_collection):
	# pages = mongo_db_collection.find_one({'term':search_term})['pages'].sort('rlink')
	# return [page['url'] for page in pages]
	record = mongo_db_collection.find_one(search_term)
	if record: 
		pages = record['pages'] # in case where _id: search_term and entry = {_id: term, pages: [(url1,score),(url2,score),etc.]}
		links = [elem[0].encode('ascii','ignore') for elem in sorted(pages,key=lambda page: page[1],reverse=True)]
		print "\r\n------------Results--------------\r\nTotal hits: %s"%len(links)
		for link in links:
			print link
	else: 
		print "The search term %s does not currently appear in the index"%search_term
	# return [page[0] for page in sorted(pages,key=lambda page: page[1])] #unsorted
	
