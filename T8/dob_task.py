def process_text(file_path):
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
file_path = "T8\DOB.txt"

# Call the process_text function with the file path
process_text(file_path)
