import crawler
import indexer
import query

if __name__ == '__main__':
	c = crawler.BFS_Crawler()
	# p = indexer.Page('http://www.lemonde.fr')
	db = c.simple_index
	# c.update_index(p)
	term = raw_input('Please enter a search term:\t')
	query.query(term,db)