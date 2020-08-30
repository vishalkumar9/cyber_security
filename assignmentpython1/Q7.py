#Write a program that creates a list of tuples for all the numbers in a given limit and indicate whether
#number is Prime or Non Prime. Let’s suppose limit is 7 so list should be created in the following way -
#[(2,Prime),(3,Prime),(4,Non Prime),(5,Prime),(6,Non Prime),(7,Prime)]


def countPrimes(num):
    if num > 1:
        for i in range(2, num):
            if (num % i)==0:
                break
        else:
            return True 
    else:
        return False

def create_tuple(arr):
    res=[]
    for i in arr:
        if countPrimes(i) == True:
            res=res+[(i,'prime')]
        else:
            res=res+[(i,'nonprime')]    
    print(res)

arr=[]
l = int(input("Enter lowest value : ")) 
h= int(input("enter highest value: "))
for i in range(l,h+1): 
    arr.append(i)    
create_tuple(arr)
