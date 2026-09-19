print("=== Smart School Day Planner ===\nAnswer 3 quick questions and I will plan your day!\n")

day = input("What day is it? (Monday to Sunday): ").strip().capitalize()
weather = input("What is the weather? (sunny / rainy / cloudy): ").strip().lower()
done = input("Is your homework done? (yes / no): ").strip().lower() == "yes"
is_weekend = day in ("Saturday", "Sunday")

print(f"\n=== Your Plan for {day} ===\n" + "-" * 35)

day_types = {
    "Saturday": "Weekend - enjoy your free time!",
    "Sunday": "Weekend - enjoy your free time!",
    "Monday": "First day of the week. Pack your weekly planner.",
    "Friday": "Last school day. Return library books today.",
    "Tuesday": "Regular school day. Stay focused!",
    "Wednesday": "Regular school day. Stay focused!",
    "Thursday": "Regular school day. Stay focused!",
}
print(f"Day type    : {day_types.get(day, 'Day not recognised. Please check the spelling.')}")




if weather == "sunny" and done:
    print("After school: Head to the park - great weather and homework is done!")

if weather in ("rainy", "cloudy"):
    print("Weather tip : Pack your umbrella - it may get wet outside.")

if not done:
    print("Homework    : Not done yet. Finish it before going out!")

if weather == "rainy" and not done:
    print("Best plan   : Stay in, finish homework, then watch your favourite show.")
elif weather == "sunny" and done and not is_weekend:
    print("Best plan   : All set for a great school day - you are prepared!")
elif is_weekend and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")

print("\nPlan complete! Have a wonderful day!")