# Nikhil Gupta
# 19 May 2020
# Program to depict use of dictionaries in Python
#
green_alien = {'color':"green",'life':20,'points':10}
#              ( key  : value ) pair
#
print(green_alien['color'])
print (green_alien['life'])
print(green_alien['points'])
new_points = green_alien['points']
print(f"Killed alien_0 & earned {new_points} points")
#
# Adding new key-value pair
#
green_alien['friend'] = "red_alien"
print(green_alien)
#
# Starting with empty dictionary
#
red_alien = {}
red_alien['color'] = "red"
red_alien['life'] = 30
red_alien['points'] = 15
red_alien['friend'] = "green_alien"
print(red_alien)
#
# Modifying values in dictionary
#
green_alien['life'] = 25
print(green_alien)
#
# Deleting key-value pair
#
del green_alien['friend']
print(green_alien)
print("Red alien is not my friend anymore!")
#
# using get() method instead of accessing values via keys
# doesnt throw error if specified key is not present 	
#
friend = green_alien.get('friend','I dont have any friends!')
print(friend)
#
# Looping through key-value pairs in dictionary
# using items()
#
for key,value in red_alien.items():
	print(f"Key: {key}")
	print(f"Value: {value}")
#
# Accessign key and value individually
#
for key in red_alien.keys():
	print(key)
for value in red_alien.values():
	print(value)
for key in sorted(red_alien.keys(),reverse = True):
	print(key)
#	
# List of Dictionaries
#
aliens = [green_alien,red_alien]
for alien in aliens:
	if alien['color']== "green":
		print("I am a green alien!")
	else:
		print("I am not a green alien!")
#
aliens = []
for alien_number in range(10):
	new_alien = {'color':"green",'life':20,'points':10,'friend':"yellow_alien"}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)

print(f"Total aliens = {len(aliens)}")
#
# List in a Dictionary
#
favorite_languages = {
'nikhil': ['python', 'ruby'],
'sarah': ['c'],
'gautam': ['ruby', 'go'],
'saurav': ['python', 'haskell'],
}
for name,languages in favorite_languages.items():
	print(f"{name.title()}'s favourite language is: ")
	for language in languages:
		print(f"{language.upper()}")
	print()
#
#	Dictionaries in Dictionary (Complicated) 
#
users  = {'ngupta':{'first':"Nikhil",
					'last': "Gupta",
					'location':"netherlands"	
					},
			'pdahiya':{'first':"Paras",
					'last': "Dahiya",
					'location':"germany"	
					}			
		 }
for username,user_info in users.items():
	print(f"Username: {username}")
	fullname = f"{user_info['first']} {user_info['last']}"
	location = f"{user_info['location']}" 
	print(f"Full name: {fullname.title()}")
	print(f"Location: {location.title()}")
#	