#define a function that takes index point as argument to sum
def sum_recursion(list, num):
    #base case
    if num ==0:
        return list[0]
    else:
        #recursive case
        return list[num]+ sum_recursion(list, num-1)

# #example    
# print(sum_recursion([1,2,3,4], 3))