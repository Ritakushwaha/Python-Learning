# Modified binary search to find last occurance of an element in a sorted array

def binary_search_find_first_occurance(arr, elem):
	result = -1
	low = 0
	high = len(arr)-1

	while (low<=high):
		mid = (low+high)//2
		if arr[mid] == elem:
			# to find the last occurance we need to keep searching towards the right
			result = mid 
			low = mid+1
		elif elem > arr[mid]:
			low = mid + 1
		else:
			high = mid -1
	return result

if __name__ == "__main__":
	arr = [2,4,10,10,10,18,20]
	res = binary_search_find_first_occurance(arr, 10)
	print(res)