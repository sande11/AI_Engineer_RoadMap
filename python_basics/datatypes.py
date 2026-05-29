# In Python, the data type is set when you assign a value to a variable:
# List
fruits = ["apple", "orange", "banana", "coconut"]
# print(fruits)
# accessing list
# using index[]
# print(fruits[0])
# first 3 elements
# print(fruits[0:3])
# using a step and also inverted
# print(fruits[::2])
# print(fruits[::-2])

# iterate with for loop
# for fruit in fruits:
#     print(fruit)

# change item value by refering to the index number

# fruits[1] = "nthochi"
# print(fruits)

# add list items (to append items)
# fruits.append("cherry")
# print(fruits)

# To insert a list item at a specified index, use the insert() method.
# fruits.insert(1, "grape")
# print(fruits)

# To append elements from another list to the current list, use the extend() method.
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# The remove() method removes the specified item but to remove an element on particular index use .pop(1) 
# if you dont specify an index .pop() removes the ;ast item while clear() empties the entire list
# fruits.remove("grape")
# print(fruits)

# list comprehension
# offers a shorter syntax when you want to create a new list based on the values of an existingg list
# eg based on a list of fruits, you want a new list containing only the fruits with the letter "a" in the name

# fruits = ["apple", "orange", "banana", "coconut"]
# newList = []

# for fruit in fruits:
#     if "a" in fruit:
#         newList.append(fruit)

# print(newList)

# OR 

# newList = [fruit in fruit in fruits if "a" in fruit]

# sort()
# used to sort list alphanumerically, ascending by default
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# sort descending
# to sort descending
thislist.sort(reverse=True)

# copy a list
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# join lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Tuple
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
mytuple = ("apple", "banana", "cherry")

# SETS
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed. do not allow duplicates
# Once a set is created, you cannot change its items, but you can remove items and add new items.
# Duplicate values will be ignored
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset)) #check length 

# Method	Shortcut	Description
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns True if NO items of this set is present in another set
# issubset()	<=	Returns True if all items of this set is present in another set
#  	<	Returns True if all items of this set is present in another, larger set
# issuperset()	>=	Returns True if all items of another set is present in this set
#  	>	Returns True if all items of another, smaller set is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others
