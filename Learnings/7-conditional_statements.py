# Nikhil Gupta
# 19 May 2020
# Programs to demonstrate conditional statements
#
my_car = "toyota fortuner"
if my_car != "hyundai creta":
	print("Thats not my creta!")
#
# if-else
#
cars = ["audi","bmw","maruti","hyundai"]
for car in cars:
	if car == "audi":
		print(car.upper())
	else:
		print(car.title())
#
# if-elif-else, and
# 
age = 18;
if age < 16:
	print("You are not eligible for admission.")
elif age >16 and age <19:
	print("You are eligible for admission! Pay $21")
else:
	print("You are eligible for admission! Pay $28")
#
# using "or"
#
light_color = "Purple"
if light_color == "Red" or light_color == "Purple":
	print(f"I need {light_color} color light.")
#
# conditionals in multiple Lists
#
super_car = ["audi","bugati"]
for car in cars:
	if car in super_car:
		print(f"I have a {car.upper()}")
	else:
		print(f"{car.title()}")	
#
current_users = ["Nikhil","Abhimanyu","Pratap","Tanya"]
new_users = ["Dhriti","Punnet","Pratap"]
for user in new_users:
	if user	in current_users:
		print(f"This username is already taken! {user}")
	else:
		print(f"Welcome to the club {user}!")
#
# Empty List checking with if statement
#
problems_in_life = []
if problems_in_life:
	print("Your hardwork will overcome your problems!")
else:
	print("Hurray! All problems solved.")
#