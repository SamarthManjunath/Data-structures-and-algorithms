#Implementation of remove duplicates from a list using hash tables
# O(N)

def remove_duplicates(arr):
	remDup = dict() #create a dictionary
	for i in arr:
		remDup[i] = 0 #create a key with 0 value
	
	return set(remDup.keys()) #set is used to retrieve only unique keys


#testcase
dataset = ["orange", "apple", "orange", "apple", "mango", "mango", "apple", "orange"]
print("With duplicates")
print(dataset)
print("Without duplicates")
result = remove_duplicates(dataset)
print(result)# orange, apple, mango