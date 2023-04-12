# Ask the user for the number of years
num_years = int(input("Enter the number of the years: "))

# Initialize a list to hold the total rainfall for each year
total_rainfall = []

# Iterate over each year
for year in range(1, num_years+1):
    # Initialize a list to hold the rainfall for each month of the year
    rainfall_per_month = []
    
    # Ask the user for the rainfall for each month of the year
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall amount for the month-{month}: "))
        rainfall_per_month.append(rainfall)
    
    # Calculate the total rainfall for the year
    total_year_rainfall = sum(rainfall_per_month)
    total_rainfall.append(total_year_rainfall)
    
    # Calculate the average monthly rainfall for the yearss
    avg_monthly_rainfall = total_year_rainfall / 12
    
    # Print the results for the year
    print=("For 12 months")
    print(f"\nTotal rainfall for year {year}: {total_year_rainfall} cm")
    print(f"Average monthly rainfall for year {year}: {avg_monthly_rainfall} cm")

# Calculate the overall average monthly rainfall
overall_avg_monthly_rainfall = sum(total_rainfall) / (num_years * 12)

# Print the overall average monthly rainfall
print(f"\nOverall average monthly rainfall: {overall_avg_monthly_rainfall} cm")
