import os
def process_text(file_name):
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_path = os.path.join(current_dir, file_name)
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Read each line from the file
        lines = file.readlines()

    # Section One: Print the first two words of each line
    print("Section One: First two words of each line")
    for line in lines:
        # Split the line into words
        words = line.strip().split()
        # Print the first two words, if available
        if len(words) >= 2:
            print(words[0], words[1])

    # Section Two: Print the last two words of each line
    print("\nSection Two: Last two words of each line")
    for line in lines:
        # Split the line into words
        words = line.strip().split()
        # Print the last two words, if available
        if len(words) >= 3:
            print(words[-3], words[-2], words[-1])

# File path of the text file
file_name = "DOB.txt"

# Call the process_text function with the file path
process_text(file_name)
