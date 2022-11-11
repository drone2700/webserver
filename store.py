import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    categories = r.json()
    print(r.status_code)
    print(r.text)

    for category in categories:
        print(category['name'])
