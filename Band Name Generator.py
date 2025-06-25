print("🪕 Welcome To The Band Name Generator 🎶 \n")

while True:
    print("Whats The Name Of The City You Grew Up \n")
    city = input("-> ")
    if city != "":
        city.title()
        break
    else:
        print("You Have Not Entered Anything Please Enter Something")

while True:
    print("\nPlease Enter The Name Of The Pet You Have 🐾 \n")
    pet = input("-> ")
    if pet != "":
        pet.title()
        break
    else:
        print("You Have Not Entered Anything Please Enter Something\n")

connectors = ["& The", "Vs", "With", "Featuring"]

for i in range(len(connectors)):
    connector = connectors[i]
    if connector in connectors:
        band_name = pet+" "+connector+" "+city
    else:
        band_name = city+" "+connector+" "+pet

    print(f"{i+1}. {band_name}\n")

print("🕺 Keep Rocking! 👯‍♀️ \n Run The Program Once Again For More Interesting Names 🤙 ")