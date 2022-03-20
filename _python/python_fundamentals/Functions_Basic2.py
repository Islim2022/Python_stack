# Countdown
def countdown(num):
    num_list = []
    for i in range (num,-1,-1):
        num_list.append(i)
    return num_list
print(countdown(12))

# Print and Return
def print_return(num_list):
    print(num_list[0])
    return num_list[1]
print(print_return([1,4]))

# First Plus Length
def first_plus_length(nums_list):
    return nums_list[0] + len.nums_list
print(first_plus_length([1,2,3,4,5]))

# Values Greater Than Second
def greater_than_second(num_list):
    new_list = []
    second_value = num_list[1]
    for i in range (len(num_list)):
        if num_list[i] > second_value:
            new_list.append(num_list[i])
    print(len(new_list))
    return new_list
print(greater_than_second([1,4,6,3,2,7]))

#This Length, that Value
def this_length_that_value(length,value):
    new_list = []
    for i in range(length):
        new_list.append(value)
    return new_list
print(this_length_that_value(4,7))