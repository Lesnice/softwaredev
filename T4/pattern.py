# Define the number of rows
num_rows = 5

# Iterate through each row
for i in range(1, 2*num_rows):
    # Calculate the number of stars to print for each row
    if i <= num_rows:
        stars = i
    else:
        stars = 2*num_rows - i

    # Print the stars for the current row
    print("*" * stars)
