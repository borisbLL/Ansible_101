#sample py
import falcon
import MySQLdb
import os

class QouteResource:

	def on_get(self, req, resp):
	"""Handles GET requests"""

	resp.content_type = 'text/html'

	try:
			db = MySQLdb.connect(host="dbserver",
								 user="ansibletutorial",
								 password=os.environ['databasepassword'],
								 db="ansibletutorial")

	except:
		resp.body = '<html><head><title>Error</title></head><body><h1>Database not available!</h1></body></html>'
		return

	cur = db.cursor()
	cur.execute("SELECT quote, author FROM quotes ORDER BY RAND() LIMIT 1")
	data = cur.fetchone()

	resp.body = '<html><head><title>Quote of the day</title></head><body><h1>{}</h1>-- {}</body></html>'.format(data[0], data[1])
	

	app = falcon.API()
	app.add_route('/', QuoteResource())
