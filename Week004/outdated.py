def main():
    loop = 1

    while loop == 1:
        try:
            dat = input("Date: ")

            if "/" in dat:
                m,d,y = dat.split("/")
                m = int(m)
                d = int(d)
                if 0 < d <= 31 and 0 < m <= 12:
                    print(f"{y}/{m:02d}/{d:02d}")
                    loop = 0
                else:
                    loop = 1
            else:
                if "," in dat:
                    dat = dat.replace(",","")
                m, d, y = dat.split(" ")
                d = int(d)
                match m.lower():
                    case "january":
                        m = "01"
                    case "february":
                        m = "02"
                    case ("march"):
                        m = "03"
                    case "april":
                        m = "04"
                    case "may":
                        m = "05"
                    case "june":
                        m = "06"
                    case "july":
                        m = "07"
                    case "august":
                        m = "08"
                    case "september":
                        m = "09"
                    case "october":
                        m = "10"
                    case "november":
                        m = "11"
                    case "december":
                        m = "12"
                    case _:
                        loop = 1
                if 0 < d <= 31 and 0 < int(m) <= 12:
                    print(f"{y}/{m}/{d:02d}")
                    loop = 0
                else:
                    loop = 1
        except:
            loop = 1


main()
