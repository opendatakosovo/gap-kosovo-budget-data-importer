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
		
		previous_column1 = ''
		previous_column2 = ''
		previous_column3 = ''
		previous_column4 = ''
		
		# Iterate through the rows, retrieve desired values.
		for row in reader:
			
			institute = row[4] # Column name: Instituti
			group_name = row[5] # Column name: GROUPNAME
			
			column1 = row[7] # Column name: Kolona 1
			column2 = row[8] # Kolona 2
			column3 = row[9] # Kolona 3
			column4 = row[10] # Kolona 4
			
			amount = row[11] # Shuma
			
			# Bah, need to figure out how to do this recursively.
			
			
