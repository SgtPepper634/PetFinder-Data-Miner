from pymongo import MongoClient
import os

MONGO_CONNECTION_STRING = os.environ.get('MONGO_CONNECTION_STRING')

client = MongoClient(MONGO_CONNECTION_STRING)
db = client['petfinder_raw_data']
dog_collection = db['dogs']
cat_collection = db['cats']
record_collection = db['records']

def insert_dogs(dogs):
  dog_collection.insert_many(dogs)


def get_last_scraped_publish_date(animalType):
  animal_scrape_record = record_collection.find_one({'animalType': animalType})
  print('\nMongo Record', animal_scrape_record)
  return animal_scrape_record['lastScrapedAnimalPublishDate'].isoformat()
