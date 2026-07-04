import json 
import sys 
import requests 

def bitPrice():
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=59249b678609eff843f33244db462e792aa78863774049d13cb8a618f2b91f45"
    )

    o = response.json()
    rate = float(o["data"]["priceUsd"])

    return rate

def main():
    num = float(sys.argv[1])
    amount = num * bitPrice()
    print(f"${amount:,.4f}")

if len(sys.argv) != 2:
    sys.exit("Too few arguments")

try:
    main()

except:
    sys.exit("Enter a number only")
