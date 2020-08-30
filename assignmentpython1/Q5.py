# Write a Python function to multiply all the numbers in a list and return the result.

def multiplyList(myList) : 
      
    # Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result  

my_list = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    my_list.append(ele)
print(multiplyList(my_list))
