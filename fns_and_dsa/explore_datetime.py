from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Display the result
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    try:
        # Ask the user for number of days to add
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate the future date
        future_date = datetime.now() + timedelta(days=days_to_add)
        # Format and display the future date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()