def is_odd(n):
    return n % 2 == 1

def main():
    n = int(input("Enter a number: "))
    if is_odd(n):
        print("The number is odd.")
    else:
        print("The number is even.")

main()

