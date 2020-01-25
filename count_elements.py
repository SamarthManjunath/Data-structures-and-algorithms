#Implementation of count elements using hash tables
# O(N)

def count_elemets(arr):
	countElements = dict()
	for i in arr:
		if i in countElements.keys():#checks if element is already a key
			countElements[i] += 1 #if true, it is incremented by 1
		else:
			countElements[i] = 1 # else, it is set as 1, new element

	return countElements

#Test case
dataset = ["orange", "apple", "orange", "apple", "mango", "mango", "apple", "orange"]
result = count_elemets(dataset) #function call
print(result) #orange: 3, apple: 3, mango: 2