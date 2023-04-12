# Define the number of rows for the pattern
num_rows = 8

# Use nested for loops to print the pattern
for i in range(num_rows):
    if i == 0:
        print("")
    else:
        # Print a "#" for the first column
        print("#", end="")
        # Print a space for each column after the first one and before the last one
        for j in range(1, i):
            print(" ", end="")
        # Print a "#" for the last column
        print("#")
