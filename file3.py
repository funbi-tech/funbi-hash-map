from file1 import extract__phone_data

def get_phone_call():
    new_result = extract__phone_data()
    print(new_result)
    new_result1 = new_result[0]
    new_result2 = new_result[1]
    new_result3 = new_result[0]
    return {'color':new_result1,'price':new_result2,'price':new_result3}


rr = get_phone_call()
print(rr)












