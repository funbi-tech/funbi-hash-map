
def remove_last_work(my_dictionary):
    my_dictionary.popitem()

    return my_dictionary

value = {"color":"pink","language":"english","age":70,"brand":"gucci","amount":80}
print(remove_last_work(value)) 

