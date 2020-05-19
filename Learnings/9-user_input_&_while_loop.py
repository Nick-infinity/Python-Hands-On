# Nikhil Gupta
# 19 May 2020
# Program to depict use of while loop & taking user input
#
message = input("Enter your name: ")
print(f"Hello, {message}!")
#
prompt = "We can personalise our greetings if you tell use your name."
prompt += "\nWhat is your name? "
name = input(prompt)
print(f"Hello, {name}")
#
# Using int to convert strings to integer type
#
age = input("How old are you? ")
age = int(age)
print(age+1)
#
dinner_members = input("How many members are there?" )
dinner_members = int(dinner_members)
if dinner_members%2:
	print("You all are welcome!")
else:
	print("Sorry, We have seat for odd number of members.")
#
# while loop
#
counter = 1
while counter <= 5:
	print(counter)
	counter += 1	
#
# simple loop exit mechanism
#
prompt = "Tell me your age and i will add 5 to it."
prompt += "\nEnter 'quit' to exit the program.\n"
age = ""
while age != 'quit':
	age = input(prompt)
	if age != 'quit':
		age = int(age)
		age += 5
		print(f"5 years later your age will be {age}")
#
# Let me tell you how to use Flags
# say "active" flags
prompt = "We can personalise our greetings if you tell use your name."
prompt += "\nWhat is your name? "
active = True
while active:
 message = input(prompt)
 if message == 'quit':
 	active = False
 else:
 	print(message)
#
# Using break
#
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}")	
#
current_number = 0
while current_number < 10:
	current_number += 1	
	if current_number % 2 == 0:
		continue
	print(current_number)
#
# while loop in lists	
#
unverfied_users = ['jayant','samridh','riya']
confirmed_users = []
while unverfied_users:
	current_user = unverfied_users.pop()
	prompt = f"Do you want to confir user {current_user}? "
	choice = input(prompt)
	if choice == 'yes':
		confirmed_users.append(current_user)
print(confirmed_users)
#
# Removing duplicate values from lists
#
veggies = ['tomato','potato','onion','cabbage','potato','carrort']
while 'potato' in veggies:
	veggies.remove('potato')
print(veggies)	
#
# Filling dictionaries with looping
#
responses = {}
active = True
asking_name = "What is your name? "
car_choice = "Which car would you like to drive? "
repeat_choice = "Would you like to let another person reposnd? (yes/no) "
while active:
	name = input(asking_name)
	car = input(car_choice)
	responses[name]=car
	repeat = input(repeat_choice)
	if repeat == 'yes':
		active = True
	elif repeat =='no':
		active = False
print("Polling has ended!")
for key,value in responses.items():
	print(f"{key} would like to drive {value} car.")
print(responses)
#