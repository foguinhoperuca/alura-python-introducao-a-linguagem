import json
import requests
from typing import Any, Dict


URL: str = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'


def get_remote_data(url: str = URL, output: str = 'remote_data.json') -> None:
    response: requests.Response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print('Got response status code 200!!')
        json_data: Any = response.json()
        data: Dict = {}
        for item in json_data:
            restaurant_name_company = item['Company']
            if restaurant_name_company not in data:
                data[restaurant_name_company] = []

            data[restaurant_name_company].append({
                'item': item['Item'],
                'price': item['price'],
                'description': item['description']
            })
    else:
        print(f'Response code is not 200!! {response.status_code=}')

    for restaurant_name, restaurant_data in data.items():
        filename: str = f'data/alura_{restaurant_name}.json'
        with open(filename, 'w') as restaurant_file:
            json.dump(restaurant_data, restaurant_file, indent=4)
