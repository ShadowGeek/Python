def main ():
    try:
        fname = input("Enter file name: ").strip().lower()
        name, ext = fname.split(".")

        match ext:
            case ("gif" | "jpg" | "jpeg" | "png"):
                print("image/" + ext)
            case ("pdf" | "zip"):
                print("application/" + ext)
            case ("txt"):
                print("text/plain")
            case _:
                print("application/octet-stream")

    except:
        print("application/octet-stream")


main()