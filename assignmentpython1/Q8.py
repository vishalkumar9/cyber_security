#Write a program that creates a dictionary for all the numbers in a given limit and indicate whether
#number is Prime or Non Prime. Let’s suppose limit is 7 so list should be created in the following way -
#{2:”Prime”,3:”Prime”,4:”NonPrime”,5:”Prime”,6:”NonPrime”,7:”Prime”} Once dictionary is created,
#delete all the Non-Prime key-value pairs and print their counts on output screen.

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
    count = 0
    res=[]
    for i in arr:
        if countPrimes(i) == True:
            res=res+[(i,'prime')]
        else:
            res=res+[(i,'nonprime')]
            count=count+1    
    print(res)

    my_list=list(res)
    result = [i for i in my_list if i[1] == 'nonprime']
    print(str(result))
    print(count)

arr=[]
l = int(input("Enter lowest value : ")) 
h= int(input("enter highest value: "))
for i in range(l,h+1): 
    arr.append(i)    
create_tuple(arr)
