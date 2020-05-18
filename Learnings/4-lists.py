# Nikhil Gupta
# 18 May 2020
# This progeam covers python lists
#
trees = ["mango","banyan","neem"]
print(trees)
print(f"The fruit giving trees is {trees[0].title()} tree.")
#
# -1 for last element and so on
print(f"The last tree in list is {trees[-1]}")
#
print(f"I can even print second last element ie {trees[-2]}")
#
# Modifying the list
#
trees[0] = "papaya"
print(trees)
#
# Adding an element in the list
#
trees.append("mango")
print(trees)
#
#Inserting element at position
#
trees.insert(1,"peepal")
print(trees) 
trees.insert(-1,"sandal")
print(trees)
#
# Deleting the element form the list
#
del trees[-2]
print(trees)
#
# pop() - removes last element from listbut stores it for later use
#
popped_item = trees.pop()
print(trees)
print(popped_item)
# pop() can be used with index
print(f"The first trees of the list was {trees.pop(0).title()}")
print(trees)
#
# Remove the item by value and not index but only first occurence
# if more than 1 occurences then use loop
trees.remove("neem")
print(trees)
#
# Organising the lists
#
trees = ['papaya', 'peepal', 'banyan', 'neem', 'sandal', 'mango']
trees.sort()
print(trees)
trees.sort(reverse = True)
print(trees)
#
trees = ['papaya', 'peepal', 'banyan', 'neem', 'sandal', 'mango']
print("The sorted list is ")
print(sorted(trees))
# reverse sorted()
print(sorted(trees,reverse=True))
print("The original list is again ")
print(trees)
trees.reverse()
print(f"The reverse list is ")
print(trees)
#
# Length of the list
print(len(trees))
#




