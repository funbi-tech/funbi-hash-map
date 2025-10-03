# without hash_map which is accurate, this way i can access all the element in the list
def two_sum(my_list, target):
    my_list = (my_list[0], my_list[1])
    target = 16
    return my_list,target
my_list = [9,7,5,3,1]
target = 16
my_list1 = two_sum(my_list, target)
print(my_list1)

# using hash_map for the first time with a little difficulty
def two_sum_with_hash_map(my_list, target):
    my_list1 = {}
    for num in my_list:
        list2 = (target, my_list)
        if list2:
            return (list2, num)
        my_list1[num] = num
        return f"invalid"

my_list = [1,2,3,4,5]
target = 3 
result = two_sum_with_hash_map(my_list, target)
print(result)



