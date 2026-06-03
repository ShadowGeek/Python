repeat = 1
firstgreeting = 1

while repeat == 1:
    if firstgreeting == 1:
        response = input("Hello, what can I help you with? ").strip().lower()
        firstgreeting = 0
    else:
        response = input("Anything else I can help you with? ").strip().lower()

    if "good" in response:
        print("Glad to hear it! ")
    elif "bad" in response:
        print("Sorry to hear that. ")
    elif response == "stop":
        print("Goodbye. ")
        repeat = 0
    else:
        print("Thanks for sharing. ")

