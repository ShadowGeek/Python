def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    diners = int(input("How many people are paying? "))
    tip = dollars * percent / diners
    print(f"Each person leave ${tip:.2f}")


def dollars_to_float(d):
    d = float(d.replace("$",""))
    return d

def percent_to_float(p):
    p = float(p.replace("%", "")) / 100
    return p


main()