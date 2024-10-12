def binary_search(arr, target):
    # Define initial boundaries
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Find the middle index
        mid = left + (right - left) // 2
        
        # Check if the target is at the middle
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        # If the target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1
            
    return -1  # Return -1 if the target is not found

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
