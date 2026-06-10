def main():
    s = input("Enter filename: ")
    print(camel(s))

def camel(s):
    newText = ""

    for c in s:

        if c.isupper():
            newText = newText + ("_"+c.lower())
        else:
            newText = newText + (c)
        end = ""

    return newText

main()
