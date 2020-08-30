#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False


def has33(nums):
    for i in range(len(nums)):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

arr=[]
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input())
    arr.append(ele)
    
print(has33(arr))
