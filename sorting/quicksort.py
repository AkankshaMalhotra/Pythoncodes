def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot=(len(arr)/2)
	left=[x for x in arr if x< arr[pivot]]
	middle=[x for x in arr if x==arr[pivot]]
	right=[x for x in arr if x>arr[pivot]]
	return(quicksort(left)+middle+quicksort(right))

def main():
	print("enter array by seperating numbers by a space")
	str_arr = raw_input().split(' ')
	arr = [int(num) for num in str_arr]
	print(quicksort(arr))


if __name__ == '__main__':
	main()
