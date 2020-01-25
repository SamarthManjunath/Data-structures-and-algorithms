#Implementation of unordered search or Linear search
#Time complexity: O(N)

def unordered_search(arr, item):
	for i in range(0, len(arr) - 1):
		 if i == item:
		 	print("{} is present".format(item))
		 	return
	print("{} is not present".format(item))


#test case
dataset = [10, 3, 5, 2, 1, 7, 4] #unordered list of numbers
print(dataset)
unordered_search(dataset, 5) # to find if 5 is there in dataset, true
unordered_search(dataset, 4) #to find of 6 is there in dataset, false