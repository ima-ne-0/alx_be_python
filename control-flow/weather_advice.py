# weather_advice.py

# Demander la météo à l'utilisateur
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Vérifier la condition et donner un conseil
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
