import requests


def extract__phone_data():
    url = "https://api.restful-api.dev/objects"

    response = requests.get(url)
    result = response.json()
    # print(result)
    #result1 = result[7]["data"]['Strap_color']
    #result2 = result[8]["data"]['Description']
    #result3 = result[12]["data"]['Generation']
    #result4 = result[9]["data"]['Capacity']
    rr = result[0]['data']['color'],result[3]['data']['price'],result[0]['data']['Price']
    return rr
    # print(result)


rr = extract__phone_data()
print(rr)












