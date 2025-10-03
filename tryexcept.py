
import requests

try:

   def get_age_from_name():
      url = "https://api.agify.io?name=michael"

      response = requests.get(url)
      # print(type(response.json())) #response.text()
      data = response.json()

      return data

   result = get_age_from_name()
   getting_age_value =result["age"]
   getting_count_value =result["count"]
   print(getting_age_value)
     

except:
       print("somrthing is wrong somewhere")
          
       


