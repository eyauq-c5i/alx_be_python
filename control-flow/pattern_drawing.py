while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size > 0:
            break
        else:
            print("Please enter a positive integer greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Initialize row counter
row = 0

# Use while loop to iterate through rows
while row < size:
    # Use for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1