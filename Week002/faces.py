def main():
    words = input("How are you today? ")
    print(convert(words))

def convert(msg):
    msg = msg.replace(":)","🙂").replace(":(","🙁")
    return msg

main()
