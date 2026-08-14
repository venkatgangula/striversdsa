
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

