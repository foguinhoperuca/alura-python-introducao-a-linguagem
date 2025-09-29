from fastapi import FastAPI, Query
import requests
from typing import Any, Dict


app = FastAPI()


@app.get('/api/hello')
def hello_world():
    return {
        'Hello': 'World'
    }


@app.get('/api/restaurant/')
def get_restaurant(restaurant: str = Query(None)):
    URL: str = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response: requests.Response = requests.get(URL)
    print(response)

    if response.status_code == 200:
        print('Got response status code 200!!')
        json_data: Any = response.json()
        if restaurant is None:
            return {'data': json_data}

        restaurant_data = []
        for item in json_data:
            if item['Company'] == restaurant:
                restaurant_data.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })

        return {
            'restaurant': restaurant,
            'menu': restaurant_data
        }
    else:
        msg: str = f'Response code is not 200!! {response.status_code=} :: {response.text}'
        print(msg)
        return {'Error': msg}
