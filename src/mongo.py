from pymongo import MongoClient
from enums import Animal
from datetime import datetime
import os
from dateutil import parser

MONGO_CONNECTION_STRING = os.environ.get('MONGO_CONNECTION_STRING')

client = MongoClient(MONGO_CONNECTION_STRING)
db = client['petfinder_raw_data']
dog_collection = db['dogs']
cat_collection = db['cats']
record_collection = db['records']

def insert_animals(animals, animal_type):
  insert_response = dog_collection.insert_many(animals) if animal_type == Animal.DOG.value else cat_collection.insert_many(animals)
  most_recently_published_datetime = animals[-1]['published_at']
  print(most_recently_published_datetime, parser.isoparse(most_recently_published_datetime))
  most_recently_published_object_id = insert_response.inserted_ids[-1]
  record_collection.update_one({'animalType': animal_type}, {
    '$set': {
      'lastScrapedAnimalPublishDate': parser.isoparse(most_recently_published_datetime),
      'lastScrapedAnimalId': most_recently_published_object_id
      }
    }
  )

def get_last_scraped_publish_date(animalType):
  animal_scrape_record = record_collection.find_one({'animalType': animalType})
  last_scraped_animals_publish_date = animal_scrape_record['lastScrapedAnimalPublishDate']
  date_str =  last_scraped_animals_publish_date.isoformat() + 'Z'
  return date_str
