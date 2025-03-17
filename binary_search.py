def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2  # Calculate mid index
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Input
n = int(input("Enter number of elements: "))
arr = sorted([int(input(f"Enter element {i+1}: ")) for i in range(n)])  # Sorted input list

# Searching element
x = int(input("Enter element to be searched: "))
result = binary_search(arr, x)

# Output result
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element not present in array")
