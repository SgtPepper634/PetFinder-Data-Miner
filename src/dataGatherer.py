# from datetime import datetime
import requests
import os

BASE_URL = 'https://api.petfinder.com/v2'

s = requests.Session()

"""
Get the API token from the Petfinder API.
"""
def get_token():
    api_key = os.environ.get('PETFINDER_API_KEY')
    api_secret = os.environ.get('PETFINDER_API_SECRET')

    # Make a POST request to get the token
    response = requests.post(
        f'{BASE_URL}/oauth2/token',
        data={
            'grant_type': 'client_credentials',
            'client_id': api_key,
            'client_secret': api_secret
        }
    )

    # Convert the response to JSON and extract the token
    token = response.json()['access_token']

    return token


def get_animals(animal_type, start_datetime_iso):
    token = get_token()
    s.headers.update({'Authorization': f'Bearer {token}'})
    
    first_response = s.get(
        f'{BASE_URL}/animals',
        params={
            'type': animal_type,
            'page': 1,
            'limit': 100,
            'after': '0001-01-01T00:00:00+0000',
            'sort': '-recent'
        }
    )

    first_response_data = first_response.json()
    print(first_response_data)
    pagination_data = first_response_data['pagination']
    animal_data = first_response_data['animals']
    total_pages = pagination_data['total_pages']

    # Upload first animal data

    # Loop through the rest of the pages and do same
    #   if encounter 403 error retry with new token 

    print(animal_data)
    return animal_data
