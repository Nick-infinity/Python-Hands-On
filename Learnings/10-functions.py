# Nikhil Gupta
# 19 May 2020
# Program to depict use of functions
#
def greet_user():
	print("Hello!")
greet_user()
#
# parameters(username) & arguements('nIkHiL')
#
def greet_user(username):
	print(f"Hello, {username.title()}")	
greet_user('nIkHiL')
#
# positional arguements
#
def pets(animal_type,pet_name):
	print(f"My {animal_type}'s name is {pet_name}.")
pets('rabbit','chagan')	
#
# Keyword arguements
#
pets(pet_name='babu',animal_type='dog')
#
# Default value : add these parameters at end
#
def aliens(alien_name,alien_planet='ujitsu'):
	print(f"Hello, i am {alien_name} from {alien_planet}.")
aliens('kakarot')	
#
# Return value
#
def sum(a,b):
	a= int(a)
	b=int(b)
	return a+b
print(sum(2,4))
#
# Making arguement optional
#
def names(first_name,last_name,middle_name=''):
	if middle_name:
		print(f"{first_name.title()} {middle_name.title()} {last_name.title()}")	
	else:
		print(f"{first_name.title()} {last_name.title()}")	
names("Nikhil", "Gupta")
names("Paras","Dahiya","Kumar")
#
# Arbitary numbers of arguemnets
# makes empty tuple of arguemnents
# then fills it
#
def make_pizza(*toppings):
	print(toppings)
make_pizza("cheese","mushroom")	
#
def make_pizza(size, *toppings):
	print(size)
	print(toppings)
make_pizza("medium","cheese","mushroom")	
# 
# *args for arbitary arguements
#
# dictionary as arbitrary arguement / arbitrary keyword arguements
# **kwargs (non-specific keyword arguements)
#
def my_info(first_name,last_name,**extra_info):
	extra_info['first_name'] = first_name
	extra_info['last_name'] = last_name
	return extra_info
info=my_info('nikhil','gupta',location='netherlands',car='bmw')
print(info)
#
# passing copy of list in functions
#
pets = ['dogs','cats','hamsters']
def print_pets(pets):
	pets.append('snakes')
	print(pets)
print_pets(pets[:])	
print(pets)	
#
def car_info(manufacturer, model, **otherinfo):
	otherinfo['manufacturer'] = manufacturer
	otherinfo['model'] = model
	return otherinfo
my_car = car_info('hyundai', 'creta', color = 'white', make = '2019')
print(my_car)
#
def function():
	"""This function does nothing at all"""
#
# """ I am a multiline doc string""""
# 
# MODULES
#
""" Make a file lets say module.py
    -> modules.py contains multiple functons
	-> we need to import fucntions from modules.py to main.py
	-> this can be done in multiple ways
#
# importing whole module
	-> put main.py and module.py in same direcotry
    -> in main.py
    -> use "import module"
    -> now we can use functions from module.py in main.py
    -> syntax: module.module_function_0
#
# importing specific function from module.py
    -> syntax: from module import module_function_0,fucntion_1
#
# another way of importing all fucntuons from module.py
    -> syntax: from module import *
#
# giving function an alias
    -> syntax: from module import function_1 as f1
    -> use as function1 as f1() in main.py
#
# giving module an alias
 	-> syntax: import module as m
 	-> use m.function1() in main.py   
# 	"""
#