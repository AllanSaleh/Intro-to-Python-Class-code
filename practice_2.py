name = input("Enter your name: ")
fav_number = int(input("Enter your favorite number: "))
birth_year = int(input("What year were you born in? "))

current_year = 2025

age = current_year - birth_year
# century_age = 100 - birth_year + 2025
year_turn_100 = birth_year + 100
square_of_fav_number = fav_number ** 2

print(f"=== {name} Profile ===")
print(f"You are {age} years old!")
print(f"You will be {year_turn_100} years old in 100 years!")
print(f"Your favorite number squared is {square_of_fav_number}")

