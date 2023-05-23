import requests
import os

BASE_URL = 'https://api.petfinder.com/v2'

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