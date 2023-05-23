from dotenv import load_dotenv
from enums import Animal
from dataGatherer import *

load_dotenv()

target_animal_not_chosen = True

while target_animal_not_chosen:
  try: 
    target_animal = input('What animal do you want to collect data for from PetFinder? ').lower().capitalize()
    if target_animal != Animal.DOG.value and target_animal != Animal.CAT.value:
      raise ValueError
    else:
      target_animal_not_chosen = False
  except ValueError:
    print('Please enter a valid animal: (Dog or Cat)\n')

def main(target_animal):
  print(f'You chose {target_animal}!')
  access_token = get_token()
  print(access_token)

main(target_animal)


