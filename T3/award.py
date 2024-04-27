def calculate(swimming, cycling, running):
    # Calculate total time
    total_time = swimming + cycling + running
    return total_time

def determine_award(total_time):
    # Determine the award based on the total time
    if total_time <= 100:
        award = "Provincial Colours"
    elif total_time <= 105:
        award = "Provincial Half Colours"
    elif total_time <= 110:
        award = "Provincial Scroll"
    else:
        award = "No Award"
    return award

# Main program
def main():
    # Read in times for swimming, cycling, and running
    swimming = float(input("Enter time for swimming (in minutes): "))
    cycling = float(input("Enter time for cycling (in minutes): "))
    running = float(input("Enter time for running (in minutes): "))

    # Calculate total time
    total_time = calculate_total_time(swimming, cycling, running)

    # Determine the award
    award = determine_award(total_time)

    # Display the total time and award
    print(f"Total time taken to complete the triathlon: {total_time} minutes")
    print(f"Award received: {award}")

if __name__ == "__main__":
    main()
