# without hash_map which is accurate, this way i can access all the element in the list
def two_sum(my_list, target):
    my_list = (my_list[0], my_list[1]) 
    """good job but what if the two values are not found in the first and second parameter, 
    that would mean the algorithm wont return the data as it should
    e.g 
    if list is [8, 5, 4, 2] code will return 8 and 5 which when added together returns 13 not 16

    """
    target = 16   #declaring the target again would override the target passed by the user when calling the function
    return my_list,target
my_list = [9,7,5,3,1]
target = 16
my_list1 = two_sum(my_list, target)
print(my_list1)

def two_sum(my_list, target):  #code is flexible and can work on different lists with different targets
    # Loop through the list with index i
    for i in range(len(my_list)):
        # Loop through the *rest* of the list with index j, starting at i + 1.
        # This ensures we are always checking two different numbers.
        for j in range(i + 1, len(my_list)):
            
            # Check if the sum of the numbers at index i and j equals the target
            if my_list[i] + my_list[j] == target:
                
                # Return the actual numbers that form the sum
                return my_list[i], my_list[j]
    
    # Return None or an empty tuple if no solution is found
    return None
# print(two_sum([1,2,3],5))
        

#using hash_map for the first time with a little difficulty
def two_sum_with_hash_map(my_list, target):
    # 'seen' is initialized as a set. 
    seen = set()
    
    # Iterate through each number in the input list
    for num in my_list:
        
        # Calculate the required complement/remainder: 
        # This is the number that, when added to 'num', equals 'target'.
        remainder = target - num
        
        # Check if the 'remainder' (the complement) has been seen before.
        if remainder in seen:
            # If the complement is found, we have a solution.
            # Return the two numbers that sum up to the target.
            return remainder, num
            
        # If the complement was NOT found, add the current number to the 'seen' list.
        # This prepares it to be a complement for subsequent numbers in the list.
        seen.add(num)


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


