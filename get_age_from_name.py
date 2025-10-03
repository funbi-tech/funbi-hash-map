
import requests

def my_work(name):
    url = f"https://api.agify.io?name={name}"

    response = requests.get(url)

    res = response.json()
    print(res)
    return res

my_name = input("enter your name")

result_from_func = my_work(my_name)
my_age = result_from_func['age']
my_count = result_from_func['count']

my_final_result =  "my name is "+my_name+" my age is "+str(my_age)+" and my count is "+str(my_count)

print(my_final_result)





















