#Implementation of merge sort
#Time complexity: O(N Log N)
#Does not happen inplace

def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		
		#split the dataset into left and right arrays
		left_arr = arr[:mid]
		right_arr = arr[mid:]

		#recursively breakdown left and right arrays
		merge_sort(left_arr)
		merge_sort(right_arr)

		#merging 
		i = 0
		j = 0
		k = 0

		#if left arrays and right arrays have values
		while (i < len(left_arr) and j < len(right_arr)):
			if left_arr[i] < right_arr[j]:
				arr[k] = left_arr[i] #lowest number is added as a first element
				i += 1
			else:
				arr[k] = right_arr[j]
				j += 1
			k += 1

		#if leftarray still has values, add them to the array
		while (i < len(left_arr)):
			arr[k] = left_arr[i]
			i += 1
			k += 1

		#if rightarray still has values, add them to the array
		while (j < len(right_arr)):
			arr[k] = right_arr[j]
			j += 1
			k += 1

	return arr #final sorted array



#test case
dataset = [4, 1, 2, 3, 5, 10, 6]
print("Before Sorting")
print(dataset)
result = merge_sort(dataset)
print("After Sorting")
print(result)