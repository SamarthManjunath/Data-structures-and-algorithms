#Implemenation of ordered search, also called binary search
#Time complexity: O(Log N)

def binary_search(arr, item):
	upper = len(arr) - 1 #size of the list - 1
	lower = 0

	while lower <= upper: #until upper and lower have not crossed
		mid = (upper + lower) // 2 #average of upper and lower

		if arr[mid] == item: #if mid = item to be found
			return mid
		if item > arr[mid]: 
			lower = mid + 1
		else:
			upper = mid - 1
	
	if lower > upper: #if the item is not there in list
		return None

#testcase
dataset = [1, 2, 3, 5, 7, 9, 20] #sorted list of numbers
result1 = binary_search(dataset, 20) 
print(result1) #5
result2 = binary_search(dataset, 10)
print(result2) #None
