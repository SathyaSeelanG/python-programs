def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            print(f"Found {target} at index {i}")
            return i
    print(f"{target} not found in the   array")
n=int(input("Enter the size of the array: "))
arr=[int(input("Enter the elements: ")) for i in range(n)]
target=int(input("Enter the target element: "))
linear_search(arr,target)

