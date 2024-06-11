#higher order functions
sorted_list=sorted([1,8,3,5,26,15,10,24,11,2,7,6,9,10,12,13])
print(sorted_list)


from math import sqrt, gcd

print(sqrt(25))
print(gcd(5,9, 8,8, 17))


"""User defined functions"""


def print_line():
    print("-"*80)
    
print_line
print("We can print lines")
print_line

def print_menu(title, options):
    print_line
    print(""*(40-(len)))