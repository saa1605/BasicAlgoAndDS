import random


# Setup
array = []
for i in range(0,1000000000):
	array.append(random.randint(0,100))
array.sort()
# print array

def linear_search(array,number):
	for i in array:
		if i == number:
			return i
	else:
		return -1 


def binary_search(array,number):

	mid_point = int(len(array)/2)
	# print array[mid_point]

	#BASE CASE
	if len(array)<=1:
		if array[mid_point] == number:
			return array[mid_point]
		else:
			return -1

	#RECURSIVE CASE 
	if (array[mid_point])>number:
		return binary_search(array[:mid_point],number)
	elif (array[mid_point])<number:
		return binary_search(array[mid_point:],number)
	else:
		return array[mid_point]
print "lol"
# print binary_search(array,(1000000000-8))
# print linear_search(array,(1000000000-8))

