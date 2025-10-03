
def remove_second_value(my_dict):
    my_dict.popitem()
    dict1 = my_dict.keys()
    dict2 = my_dict.values()

    return dict1,dict2

my_dict = {"color":"green","height":"short","cast":"crew"}
my_dict = remove_second_value(my_dict)
print(my_dict)








