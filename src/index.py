from dotenv import load_dotenv
from mongo import *
from dataGatherer import *
from helperFunctions import *

load_dotenv()

def main():
  target_animal = choose_scrape_animal()
  scraping_start_point = get_last_scraped_publish_date(target_animal)
  get_animals(target_animal, scraping_start_point)
  
  

main()


