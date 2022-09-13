from flask import Flask
from flask_restful import Resource,Api,reqparse
import sqlite3
from item import handleColour,handleMemory,findCost
import os
import logging
dbFileName = 'data.db'
try:
	os.remove(dbFileName)
	print("INFO: % has been deleted." %(dbFileName))
except OSError as error:
	print("ERROR: There was an error while deleting db %s." %(dbFileName))
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS colours (colour text, price real)"
cursor.execute(create_table)
print("INFO: Created table colours in database %s" %(dbFileName))
create_table = "CREATE TABLE IF NOT EXISTS memory ( memory int, price real)"
cursor.execute(create_table)
print("INFO: Created table memory in database %s" %(dbFileName))
connection.commit()

connection.close()


app = Flask(__name__)
api = Api(app)

api.add_resource(handleColour, '/colour/<string:colour>')
api.add_resource(handleMemory, '/memory/<string:memory>')
api.add_resource(findCost, '/cost/<string:colour>/<string:memory>')
app.run(port=5000)
