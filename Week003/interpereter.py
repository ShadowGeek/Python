def main():
    equation = input("Enter the equation: ")
    x, operator, y = equation.split(" ")
    x = int(x)
    y = int(y)

    match operator:
        case "+":
            print(x + y)
        case "-":
            print(x - y)
        case "*":
            print(x * y)
        case "/":
            print(x / y)


main()