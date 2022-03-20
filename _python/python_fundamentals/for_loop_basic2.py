# Biggie_size
from itertools import count


def biggie_size(num_list):
    for i in range (len(num_list)):
        if num_list[i] > 0:
            num_list [i] = "big"
    return num_list
print(biggie_size([-1,3,5,-5]))

#Count_positives
def count_positive(num_list):
    count = 0
    for i in range(len(num_list)):
        if num_list[i] > 0:
            count += 1
# replacing the last_index with count of positive values:
    last_i= len(num_list) - 1
    num_list[last_i] = count
    return num_list
print(count_positive([3,4,-1,5,-3,-8,9]))

#Sum_total
def sum_total(num_list):
    sum = 0
    for i in range (len(num_list)):
        sum += num_list[i]
    return sum
print(sum_total([1,2,3,4,5]))

#Average
def average(num_list):
    sum = 0
    for i in range (len(num_list)):
        sum += num_list[i]
    return sum / len(num_list)
print(average([1,2,3,4,5]))

#Length
def length(num_list):
    for i in range(len(num_list)):
        return len(num_list)
print(length([1,2,3,4]))

#Minimum
def minimum(num_list):
    minimum = num_list[1]
    for i in range(len(num_list)):
        if num_list[i] < minimum:
            minimum = num_list[i]
    return minimum    
print(minimum([37,9,2,-1,-9]))

#Maximum
def maximum(num_list):
    if len(num_list) == 0:
        return False
    else:
        maximum = num_list[1]
        for i in range(len(num_list)):
            if num_list[i] > maximum:
                maximum = num_list[i]
        return maximum
print(maximum([37,9,2,-1,-9]))
print(maximum([]))

#Ultimate_analysis
#For this function, the previous functions for sum, length, max, and min could be called back
def ultimate_analysis(num_list):
    sum = sum_total(num_list)
    avg = average(num_list)
    len = length(num_list)
    max = maximum(num_list)
    min = minimum(num_list)
    analysis = {
        'SumTotal' : sum,
        'Length' : len,
        'average' : avg,
        'maximum' : max,
        'minimum' : min
    }
    return analysis
print(ultimate_analysis([37,2,1,-9]))



