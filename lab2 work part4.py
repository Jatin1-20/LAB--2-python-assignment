def print_list(lst):
    """
    Function to print all elements of a list on the console.
    """
    for element in lst:
        print(element)

# Declare and initialize the list
myNumbers = [5, 10, 15, 20, 25, 30]
GT12 = []

# Print all elements of the list
print("All numbers:")
print(myNumbers)

# Find and print all elements greater than 12
for num in myNumbers:
    if num > 12:
        GT12.append(num)

        
print("Numbers greater than 12:")
print(GT12)
