#Implementation of find max using recursion
# O(N)

def find_max(arr):
	#if there is only one element in array
	if len(arr) == 1:
		return arr[0] #max is the only element

	#if there are more elements
	ele1 = arr[0]
	ele2 = find_max(arr[1:]) #find max recursively is called again for elements 2 to end

	if ele1 > ele2:
		return ele1 #max is element 1
	else:
		return ele2 #max is element 2

#testcase
dataset = [1, 20, 200, 1000, 4, 6, 50] 
result = find_max(dataset)
print(result) #1000