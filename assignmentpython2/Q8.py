#Write a function that takes in a list of integers and returns True if it contains 007 in order
#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False



def spy_game(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            for x in range(i+1,len(nums)):
                if nums[x] == 0:
                    for y in range(x+1,len(nums)):
                        if nums[y] == 7:
                            return True

    return False                                   
arr=[]
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input())
    arr.append(ele)
print(spy_game(arr))
