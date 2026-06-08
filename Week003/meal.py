def convert(time):
    hour,minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    minute = minute/60
    return hour + minute

def main():
    time = input("What time is it? ")
    decTime = convert(time)

    if 7 <= decTime <= 8:
        print("Breakfast Time!")
    elif 12 <= decTime <= 13:
        print("Lunch Time!")
    elif 18 <= decTime <= 19:
        print("Dinner Time!")

main()

