dat = input("Date: ").strip().lower()

mon = {
    "january":"01",
    "february":"02",
    "march":"03",
    "april":"04",
    "may":"05",
    "june":"06",
    "july":"07",
    "august":"08",
    "september":"09",
    "october":"10",
    "november":"11",
    "december":"12"
}

if "/" in dat:
    # 8/15/2026
    m,d,y = dat.split("/")

    m = int(m)
    d = int(d)

    print(f"{y}-{m:02}-{d:02}")

else:
    m,d,y = dat.replace(",","").split(" ")
    d = int(d)
    print(f"{y}-{mon[m]}-{d:02}")

