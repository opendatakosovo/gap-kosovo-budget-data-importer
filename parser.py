import csv
import sys

from pymongo import MongoClient

filepath = sys.argv[1]

# Collection name will be the file name
collection_name = filepath[filepath.rindex('/')+1:filepath.rindex('.')]

# Connect to default local instance of mongo
client = MongoClient()

# Get database and collection
db = client.kosovobudget

collection = db[collection_name]

# Clear data
db[collection_name].remove({})

def parse_csv():
	'''
	Reads the KDI local election monitoring CSV file.
	Creates Mongo document for each observation entry.
	Stores generated JSON documents.
	'''
	with open(csv_filename, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		
		# Skip the header
		next(reader, None)
		
		# Bah, need to figure out how to do this recursively.
			
			
