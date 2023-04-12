def get_positive_number(prompt):
    """
    Helper function to get a positive number from the user.
    """
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                raise ValueError("Value must be positive.")
            return num
        except ValueError as e:
            print(e)

# Get the input of user
start_count = get_positive_number("Enter the starting number of organisms/species: ")
avg_increase = get_positive_number("Enter the average daily percentage increase: ")
num_days = int(get_positive_number("Enter the number of days to display the final data: "))

# Print the header
print("Day Approximate\t\t\t\t\tpopulation")
print("----------------------------------------------------------")

# Print the starting count
print(f"01\t\t\t\t\t\t{start_count:.2f}")

# Iterate over the remaining days
for day in range(2, num_days+1):
    # Calculate the new count
    new_count = start_count * (1 + avg_increase/100)**(day-1)
    
    # Print the count for the day
    print(f"{day:02}\t\t\t\t\t\t{new_count:.2f}")
