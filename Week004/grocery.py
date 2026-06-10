grocery_list = {}

while True:
    try:
        item = input("Item name: ").upper()
        grocery_list.update({item: (int(grocery_list[item])+1)})

    except EOFError:
        sorted_data_desc = dict(sorted(grocery_list.items()))

        for itm, qty in sorted_data_desc.items():
            print(f"{qty} {itm}")

        break

    except KeyError:
        grocery_list[item] = 1
        pass