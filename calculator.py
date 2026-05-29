try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print (f"{x} + {y} = {x+y}")

except ValueError:
    print("Please enter only whole numbers")