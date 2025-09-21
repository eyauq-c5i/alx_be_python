def draw_square_pattern():
    """
    Prompts the user for a positive integer and draws a square pattern of that size
    using nested loops.
    """
    while True:
        try:
            size_str = input("Enter the size of the pattern: ")
            size = int(size_str)
            if size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    i = 0
    while i < size:
        for _ in range(size):
            print("*", end="")
        print()
        i += 1

if __name__ == "__main__":
    draw_square_pattern()