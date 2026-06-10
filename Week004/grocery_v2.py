grocery_list = {}

while True:
    try:
        item = input("Item name: ").upper()

        if item not in grocery_list:
            grocery_list[item] = 1
        else:
            grocery_list[item] += 1

    except EOFError:
        grocery_list = dict(sorted(grocery_list.items()))

        for itm, qty in grocery_list.items():
            print(f"{qty} {itm}")

        break
