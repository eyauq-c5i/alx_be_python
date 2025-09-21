number = int(input("Enter a number to see its multiplication table: "))

for x in range (1, 11):
    multiply = number * x
    print(f" {number} * {x} = {multiply}")
