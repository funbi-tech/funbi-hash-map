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


# trying to modify code to return indices of two numbers
def two_sum_indices(my_list, target):
    seen = {}  # to store the nunbers and also indexes
    for index, num in enumerate(my_list):  #getting  numbers and index at the same time
        complement = target - num  # i think the code is trying to calculate the numbers that acn add up to target here
        if complement in seen:  # code is able to achieve its course here
            return [seen[complement], index]
        
    
        seen[num] = index # cant explain the line

my_list = [2,7,11,15]
target = 9
# only f string seem to work
print(f"Input: {my_list}, Target: {target}")  

print(f"Output: {two_sum_indices(my_list, target)}")


