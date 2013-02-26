import bulbs.neo4jserver as bulbs
import sys

if __name__ == '__main__':
	try:
		sys.argv[1]=='DEFINITELY'
	except IndexError:
		sys.exit("Retry with 'DEFINITELY' if you definitely want to delete your database. Completely.")
	else:
		g = bulbs.Graph()
		for vertex in g.vertices.get_all():
			g.vertices.delete(vertex._id)
		assert g.vertices.get_all() == None


