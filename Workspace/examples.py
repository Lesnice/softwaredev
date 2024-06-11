def sum_list(num_list):
    total = 0
    for num in num_list:
        total += num
        return total
    
    
def get_middle_of_list(lst):
    mid_index = len(lst)//2
    return lst[mid_index]

def get_average(grades):
    return sum(grades)/len(grades)

def get_all_students_average():
    pass