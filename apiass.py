import requests

try:
    def extract__phone_data():
        url = "https://api.restful-api.dev/objects"

        response = requests.get(url)
        print(response.json())
        data = response.json()
        #print(data[0]'name','id','data')

    
        return data

    result = extract__phone_data()
    

    #def get_phone_data():
        #return f"I love to have {getting_strap_color} alongside {getting_description} particularly from {getting_generation} with also a large {getting_capacity}"

except:
    print("something went wrong")

#result = extract_phone_data()
#result = [{'id': '1', 'name': 'Google Pixel 6 Pro', 'data': {'color': 'Cloudy White', 'capacity': '128 GB'}}, {'id': '2', 'name': 'Apple iPhone 12 Mini, 256GB, Blue', 'data': None}, {'id': '3', 'name': 'Apple iPhone 12 Pro Max', 'data': {'color': 'Cloudy White', 'capacity GB': 512}}, {'id': '4', 'name': 'Apple iPhone 11, 64GB', 'data': {'price': 389.99, 'color': 'Purple'}}, {'id': '5', 'name': 'Samsung Galaxy Z Fold2', 'data': {'price': 689.99, 'color': 'Brown'}}, {'id': '6', 'name': 'Apple AirPods', 'data': {'generation': '3rd', 'price': 120}}, {'id': '7', 'name': 'Apple MacBook Pro 16', 'data': {'year': 2019, 'price': 1849.99, 'CPU model': 'Intel Core i9', 'Hard disk size': '1 TB'}}, {'id': '8', 'name': 'Apple Watch Series 8', 'data': {'Strap Colour': 'Elderberry', 'Case Size': '41mm'}}, {'id': '9', 'name': 'Beats Studio3 Wireless', 'data': {'Color': 'Red', 'Description': 'High-performance wireless noise cancelling headphones'}}]
#extract_list = extract__phone_data#result[0]
#print(extract_list)
getting_strap_color = result[7]["data"]['Strap Colour']
getting_description = result[8]["data"]['Description']
getting_generation = result[12]["data"]['Generation']
getting_capacity = result[9]["data"]['Capacity']


#print(f"I would like to have {getting_strap_color} with{getting_description} likely from {getting_generation} with also a large{getting_capacity}")






