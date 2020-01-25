#Implementation of Bubble sort
#Time complexity is O(N ^ 2)

def bubble_sort(nums): # Sorting function
	for i in range(len(nums) - 1, 0, -1):
		for j in range(i):
			if nums[j] > nums[j + 1]:
				temp = nums[j]
				nums[j] = nums[j + 1]
				nums[j + 1] = temp
	return nums



#main
nums = [5, 3, 7, 1, 9, 2]
print("Before sorting: ", nums)
result = bubble_sort(nums) #function call
print("After sorting: ", result)
