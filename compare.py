def main():
    try:
        rating = int(input("What is your movie rating (0-100)? "))

        if rating > 100 or rating < 0:
            print("Only enter whole numbers between 0 and 100.")
        elif rating >= 90:
            print("🌟 An absolute masterpiece! Certified Fresh.")
        elif rating >= 70:
            print("👍 Pretty good! Definitely worth a watch.")
        elif rating >= 50:
            print("😐 Meh. Good for background noise while folding laundry.")
        elif rating >= 30:
            print("👎 Skip it. Save your time and money.")
        else:
            print("🗑 A cinematic disaster. Someone delete the footage.")

    except ValueError:
        print("Only enter whole numbers between 0 and 100.")
        return

main()








