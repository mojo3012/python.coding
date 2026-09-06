temp=int(input("Enter today's temperature in degree Celsius: "))
is_raining=input("Is it raining today? (yes/no): ").strip().lower()
wind_speed=int(input("Enter today's wind speed in km/h: "))
has_puddles=input("Are there puddles on the ground? (yes/no): ").strip().lower()

print("\n--- Weather assesment ---")
if temp<20:
    outfit= "jacket"
    print("It is cold today. Wear a jacket.")
else:
    outfit= "t-shirt"
    print("It is cold today. Wear a t-shirt.")

if is_raining== "yes":
    print("Bring an umbrella")

if wind_speed>30:
    needs_windbreaker="yes"
    print(f"It is windy today, wear a windbreaker over your {outfit} ")    
else:

    needs_windbreaker = "no"

    print(f"It is calm today. No windbreaker needed over your {outfit}.")
if has_puddles== "yes":
    shoes="boots"
    print("The ground is wet. Wear boots")

else:
    shoes="sneakers"
    print("The ground is dry. Wear sneakers")

print("n\--- Weather check complete ---")
print("Weather outfit picker")
print(f"Temperature:     {temp} degrees Celsius")
print(f"Outfit Chosen: {outfit}")

print(f"Raining: {is_raining}")

print(f"Windbreaker Needed: {needs_windbreaker}")

print(f"Shoes Chosen: {shoes}")

print("=" * 43)