#linear search and binary search

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            print(f"Found {target} at index {i}")
            return i
    print(f"{target} not found in the   array")


def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"{target} not found in the   array")

switch = int(input("Enter 1 for linear search or 2 for binary search: "))
n = int(input("Enter the size of the array: "))
arr = [int(input("Enter the elements: ")) for i in range(n)]
target = int(input("Enter the target element: "))
if switch == 1:
    linear_search(arr, target)
elif switch == 2:
    binary_search(arr, target)