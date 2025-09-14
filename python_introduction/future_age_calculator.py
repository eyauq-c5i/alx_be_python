# Create a Python script that asks the user for their current age
# and then calculates how old they will be in a specific future year.

# Prompt the user for their current age and store the input as an integer
current_age = int(input("How old are you? "))

# Calculate the age in 2050 (assuming the current year is 2023)
future_age = current_age + (2050 - 2023)

# Print the user's future age in the specified format
print(f"In 2050, you will be {future_age} years old.")
