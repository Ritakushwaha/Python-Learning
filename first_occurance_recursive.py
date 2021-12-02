def binary_search_find_first_occurance(arr, l, r, query, res):
	if l > r:
		return res
	mid = (l+r)//2
	if query == arr[mid]:
		res = mid
		return binary_search_find_first_occurance(arr, l, mid-1, query, res)
	elif query < arr[mid]:
		return binary_search_find_first_occurance(arr, l, mid-1, query, res)
	else:
		return binary_search_find_first_occurance(arr, mid+1, r, query, res)

if __name__ == "__main__":
	arr = [2,4,10,10,10,18,20]
	l = 0
	r = len(arr)-1
	query = 10
	res = -1
	res = binary_search_find_first_occurance(arr, l, r, query, res)
	print(res)