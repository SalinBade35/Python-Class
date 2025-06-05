import random
import math
import calendar
from datetime import datetime

# ❌ ✅ 🎉 📅 🔁 📏 📐

# 🎯 1. Guessing game from 0 to 20
number = random.randint(0, 20)
guess = int(input("Guess a number between 0 and 20: "))

if guess == number:
    print("🎉 Correct! You guessed it.")
else:
    print(f"❌ Nope! The correct number was {number}.")

print("\n--- Math Magic ---")

# 📏 2. Area of a circle and volume of a sphere
radius = float(input("Enter radius: "))

area_circle = math.pi * math.pow(radius, 2)
volume_sphere = (4/3) * math.pi * math.pow(radius, 3)

print(f"✅ Area of circle: {round(area_circle, 2)}")
print(f"✅ Volume of sphere: {round(volume_sphere, 2)}")

# 📐 3. Find angle in degrees whose sine is 0.5
angle_radians = math.asin(0.5)
angle_degrees = math.degrees(angle_radians)
print(f"✅ Angle whose sine is 0.5: {round(angle_degrees, 2)}°")

print("\n--- Calendar Time ---")

# 📆 4. Print calendar for current year
current_year = datetime.now().year
print(f"📅 Calendar for {current_year}:")
print(calendar.calendar(current_year))

# 🔁 5. Check leap year
year_to_check = int(input("Enter a year to check if it's a leap year: "))
is_leap = calendar.isleap(year_to_check)
print(f"✅ {year_to_check} is a leap year." if is_leap else f"❌ {year_to_check} is not a leap year.")
