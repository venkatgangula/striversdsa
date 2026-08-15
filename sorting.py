
#selection sorts
#minimum is first
#minimum element is selected from unsorted array and swapped with the leftmost unsorted element

arr=[9,56,8,14,24,46]
n=len(arr)
for i in range(n-1):
    min=i
    for j in range(i,n):
        if arr[j]<arr[min]:
            temp=arr[min]
            arr[min]=arr[j]
            arr[j]=temp
            
print(arr)


#bubble sort
#maximum is last
#repeatedly swap adjacent elements if they are in wrong order

arr=[9,56,20,40,24,46]
n=len(arr)
for i in range(n-1,0,-1):
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
            
print(arr)

#optimized bubble sort

arr=[1,2,3,4,5,6]
n=len(arr)
for i in range(n-1,0,-1):
    swap=0
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
            swap+=1
    if swap==0:
        break
    
            
print(arr)

#insertion sort
#takes one element from unsorted array and inserts it into sorted array at the correct position



# arr=[1,2,3,4,5,6]
arr=[9,56,20,40,24,46]
n=len(arr)
for i in range(n-1):
    j=i+1
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j=j-1
    
            
print(arr)



def check(nums):
    n=True
    for i in range(1,len(nums)-1):
        if nums[i]>=nums[i-1]:
            n=True
        else:
            n=False
            break
    return n

# merge sort
# divides the array into two halves, sorts them recursively, and then merges the sorted halves

def merge_sort(arr):
    # Base case:
    # If the array has 0 or 1 element,
    # it is already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle index
    mid = len(arr) // 2

    # Divide the array into two halves
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the left half
    left = merge_sort(left)

    # Recursively sort the right half
    right = merge_sort(right)

    # Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    result = []

    # i points to the current element of left
    # j points to the current element of right
    i = 0
    j = 0

    # Compare elements from both arrays
    while i < len(left) and j < len(right):

        # Take the smaller element
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # If elements are remaining in left,
    # add them to result
    while i < len(left):
        result.append(left[i])
        i += 1

    # If elements are remaining in right,
    # add them to result
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Example
arr = [5, 2, 8, 1, 3, 7]

print("Before sorting:", arr)

sorted_arr = merge_sort(arr)

print("After sorting:", sorted_arr)



    #          [5,2,8,1,3,7]
    #           /          \
    #       [5,2,8]       [1,3,7]
    #       /   \          /   \
    #    [5]   [2,8]    [1]   [3,7]

#     [2] + [8]       → [2,8]
# [5] + [2,8]     → [2,5,8]

# [3] + [7]       → [3,7]
# [1] + [3,7]     → [1,3,7]

# [2,5,8] + [1,3,7]
#               ↓
#         [1,2,3,5,7,8]

# Time: O(n log n)
# Space: O(n)

# quick sort
# selects a pivot element and partitions the array around it, then recursively sorts the sub-arrays

def quick_sort(arr, low, high):

    # Continue only if there are at least
    # two elements to sort
    if low < high:

        # Partition the array
        # and get the pivot's final position
        pivot_index = partition(arr, low, high)

        # Sort elements BEFORE the pivot
        quick_sort(arr, low, pivot_index - 1)

        # Sort elements AFTER the pivot
        quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):

    # Choose the last element as the pivot
    pivot = arr[high]

    # i keeps track of where the smaller
    # elements should be placed
    i = low - 1

    # Check every element from low to high-1
    for j in range(low, high):

        # If current element is smaller
        # than or equal to the pivot
        if arr[j] <= pivot:

            # Move i forward
            i += 1

            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Put the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the pivot's final position
    return i + 1


# Example
arr = [5, 2, 8, 1, 3, 7]

print("Before sorting:", arr)

quick_sort(arr, 0, len(arr) - 1)

print("After sorting:", arr)


# [5, 2, 8, 1, 3, 7]
# pivot = 7
# Smaller than 7     Pivot     Greater than 7

# [5, 2, 1, 3]         7            [8]
# [5, 2, 1, 3, 7, 8]
#              ↑
#            pivot
# [1, 2, 3, 5, 7, 8]
# Average time: O(n log n)
# Worst case: O(n²)
# Space: O(log n) average recursion stack.



