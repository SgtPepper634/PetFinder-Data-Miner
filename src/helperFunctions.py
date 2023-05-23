from enums import Animal

def choose_scrape_animal():
  target_animal_not_chosen = True

  while target_animal_not_chosen:
    try: 
      target_animal = input('What animal do you want to collect data for from Petfinder? ').lower().capitalize()
      if target_animal != Animal.DOG.value and target_animal != Animal.CAT.value:
        raise ValueError
      else:
        target_animal_not_chosen = False
    except ValueError:
      print('Please enter a valid animal: (Dog or Cat)\n')

  print(f'You chose {target_animal}!')
  return target_animal