def get_first_sorted_name(names):
    names.sort()
    name = names[0]
    return name

#arrange
names = ["Tina", "Peter", "Jack", "Jamie", "Anita"]
#act
result = get_first_sorted_name(names)
#Assert
print(result)
print(result == "Anita")