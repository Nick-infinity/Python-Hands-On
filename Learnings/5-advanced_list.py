# Nikhil Gupta
# 18 May 2020
# "Working with lists"
#
devices = ['tissot', 'whyred', 'armani', 'lavender']
turn = 1
for every_device in devices:
	print(f"{every_device.title()} was my {turn} device.")
	turn = turn +1
print("Thats all about my devices!")
#
# Indentation is really important in python
#
# 5 isn't included in range
#
for value in range(1,5):
	print(value)
for value in range(6):
	print(value)
#
# List from the range of numbers
#
numbers = list(range(10,21))
print(numbers)
# 
# Step size in range()
#
for every_evenNumber in range(2,7,2):
	print(every_evenNumber)
#
sqaures = []
for values in range(1,5,1):
	sqaures.append(values ** 2)
print(sqaures)	
#
# List Comprehension:
#
sqaures = [values ** 2 for values in range(1,5)]
print(sqaures)
#
# Min, Max, Sum of List of numbers
#
print(min(sqaures))
print(max(sqaures))
print(sum(sqaures))
#
# Creating Comprehensions Examples
#
million = [ values for values in range(1,1000001)]
print(min(million))
print(max(million))
print(sum(million))
#
cubes = [values ** 3 for values in range(1,11)]
print(cubes)
#
# Slicing the list
#
print(devices[0:3])
print(devices[:2])
print(devices[3:])
# Third arguement is for skipping
print(devices[0:4:2])
#
# Looping through slices
#
for each_device in devices[1:]:
	print(each_device.title())
#
# Copying a list
#
top_devices = devices[:]
print(top_devices)
top_devices.append("raphael")
print(top_devices)
#
# top_devices = devices just assign new variable instead of copying
# any changes made to either (same) list will be done in both (same) list/s
#


