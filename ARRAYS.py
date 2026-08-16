       #                   ARRAY
       #                     │
       #                     ▼
       #             ┌───────────────┐
       #             │ CONSTRAINTS   │
       #             └───────┬───────┘
       #                     │
       #              ┌──────┴──────┐
       #              │             │
       #           small          large
       #              │             │
       #           brute         optimize
       #                            │
       #                            ▼
       #                   ┌────────────────┐
       #                   │ WHAT IS ASKED? │
       #                   └───────┬────────┘
       #                           │
       #      ┌────────────────────┼─────────────────────┐
       #      │                    │                     │
       #      ▼                    ▼                     ▼
       #   ELEMENT              SUBARRAY                PAIR
       #      │                    │                     │
       #      ▼                    ▼                     ▼
       #  Set/HashMap       Window / Prefix Sum      HashMap
       #                                               Pointer
       #      │                    │
       #      │           ┌────────┴────────┐
       #      │           │                 │
       #      │        Positive          Negative
       #      │           │                 │
       #      │           ▼                 ▼
       #      │       Window           Prefix Sum
       #      │
       #      ▼
       # DUPLICATE?
       #      │
       #      ▼
       #     SET

       #                     ↓
       #              SORTED ARRAY?
       #                     │
       #              ┌──────┴──────┐
       #              ▼             ▼
       #             YES            NO
       #              │             │
       #              ▼             ▼
       #        2 Pointer       HashMap/Sort
       #        Binary Search

       #                     ↓
       #              COMPLEXITY CHECK
       #                     │
       #              ┌──────┴──────┐
       #              ▼             ▼
       #           O(n²) ❌      O(n)/O(logn) ✅





# Largest Element
# this function takes a list of numbers as input and returns the largest element in the list. It initializes the largest variable with the first element of the list and then iterates through the list, comparing each element to the current largest value. If a larger element is found, it updates the largest variable. Finally, it returns the largest value found.

class Solution:
    def largestElement(self, nums):
        largest=nums[0]
        for i in range(len(nums)-1):
            if nums[i]>largest:
                largest=nums[i]
        return largest


# Input: nums = [3, 3, 0, 99, -40]

# Output: 99

# Explanation: The largest element in array is 99




# second largest element
# this function takes a list of numbers as input and returns the second largest element in the list. It initializes two variables, largest and slargest, with the first element of the list and -1 respectively. It then iterates through the list, comparing each element to the current largest value. If a larger element is found, it updates both largest and slargest accordingly. If an element is smaller than largest but larger than slargest, it updates slargest. Finally, it returns the second largest value found.
# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.


# Example 1

# Input: nums = [8, 8, 7, 6, 5]

# Output: 7

# Explanation:

# The largest value in nums is 8, the second largest is 7


class Solution:
    def secondLargestElement(self, nums):
            largest=nums[0]
            slargest=-1
            for i in range(1,len(nums)-1):
                if nums[i]>largest :
                    slargest=largest
                    largest=nums[i]
                elif nums[i]<largest and nums[i]>slargest:
                    slargest=nums[i]
            return slargest

         
# 1752. Check if Array Is Sorted and Rotated
# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].

class Solution(object):
    def check(self, nums):
        n=len(nums)
        count=0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                count+=1
                if count>1:

                    return False
            
        return True

# 26. Remove Duplicates from Sorted Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1

        return i

