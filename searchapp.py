from flask import Flask,render_template,request
import crawler
import indexer
import query

app = Flask(__name__)
app.debug = True

c = crawler.BFS_Crawler()
db = c.simple_index

@app.route('/')
def home():
	links = []
	searchword = request.args.get('query', '')
	if searchword:
		links = query.query2(searchword,db)
	return render_template('index.html',query=searchword,results=links) # should else: return "I've got nothing for you"



if __name__ == '__main__':
	app.run()