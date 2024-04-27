# Initialize variables
total = 0
count = 0

# Continuously ask the user to enter a number
while True:
    num = input("Enter a number (enter -1 to stop): ")
    
    # Check if the input is "-1" to stop the loop
    if num == -1:
        break
    
    # Convert the input to a float and add it to the total
    num = float(num)
    total += num
    count += 1

# Check if any numbers were entered (excluding -1) to avoid division by zero
if count > 0: 
    # Calculate the average
    average = total / count
    print("Average of the numbers entered (excluding -1):", average)
else:
    print("No numbers entered (excluding -1).")

