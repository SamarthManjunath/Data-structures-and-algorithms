#Implementation of quicksort
#Time complexity: O(N Log N)
#Inplace sorting

def quicksort(arr, first, last): #quicksort function #dataset, 0, last
	if first < last:
		pivot_index = partition(arr, first, last) # call the partition function to find the pivot index value 
		
		quicksort(arr, first, pivot_index - 1) # resursive quicksort call on left side of pivot
		quicksort(arr, pivot_index + 1, last)# resursive quicksort call on right side of pivot


def partition(arr, first, last): #function to find the pivot index or splitting point
	pivot_value = arr[first] #choose the first element as the pivot value

	#establish the lower and upper indexes
	lower = first + 1 #since first if the pivot
	upper = last

	#start searching for the crossing point og upper and lower indexes
	done = False
	while not done:
		#advance the lower index
		while lower <= upper and arr[lower] <= pivot_value:
			lower += 1

		#decrement the upper index
		while arr[upper] >= pivot_value and upper >= lower:
			upper -= 1

		#if two index cross each other, we have found the split point
		if lower > upper:
			done = True
		else:
			temp = arr[lower]
			arr[lower] = arr[upper]
			arr[upper] = temp

	#swap the pivot and the upper value since we have found the split point
	temp = arr[first]
	arr[first] = arr[upper]
	arr[upper] = temp

	#return the upper index
	return upper

#test case
dataset = [4, 1, 2, 3, 5, 10, 6]
print("Before sorting")
print(dataset)
quicksort(dataset, 0, len(dataset) - 1) #quicksort function takes 3 parameters, dataset, first index, last index
print("After sorting")
print(dataset)





