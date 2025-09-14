# Ask the user for their current age and convert the input to an integer
current_age = int(input("Please enter your current age: "))

# Define the target year
target_year = 2050

# Get the current year
current_year = 2024  # Assuming the current year is 2024

# Calculate the age in the target year
age_in_target_year = current_age + (target_year - current_year)

# Print the result using an f-string for clear output
print(f"You will be {age_in_target_year} years old in {target_year}.")