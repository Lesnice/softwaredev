#define function taking takes list and integer and use it to find largest number

def largest_num(list):
    if len(list)==1:
        return list[0]
    else:
        #recursive case
        biggest = largest_num(list[1:])
        return list[0] if list[0]> biggest else biggest
    
