
import requests

def extract_phone_data():
    url = "https://api.restful-api.dev/objects"

    response = requests.get(url)

    res = response.json
    print(res)
    return res

extract_phone_data()


