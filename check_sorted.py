#Implementing if the list is sorted or not
#Time Complexity: O(N)

def check_sorted(arr):
	# for i in range(0, len(arr) - 1):
	# 	if arr[i] >= arr[i + 1]: #checking for ascending property
	# 		return False
	# return True

	#using list comprehension
	return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

#Test case
dataset1 = [1, 2, 3, 5, 7, 9, 20] #sorted list of numbers
dataset2 = [10, 3, 5, 2, 1, 7, 4] #unordered list of numbers
print(check_sorted(dataset1)) #true
print(check_sorted(dataset2)) #false

