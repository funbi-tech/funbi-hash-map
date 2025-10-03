from crox import extract__phone_data

def phone_call():
    new_result = extract__phone_data
    print(new_result)
    new1 = new_result[7]
    new2 = new_result[8]
    new3 = new_result[12]
    new4 = new_result[9]
    return f"strap_color:{new1},description:{new2},generation:{new3},capacity:{new4}"

#my_result = phone_call()

print(phone_call())













