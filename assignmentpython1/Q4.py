#Write a Python function that takes a list and returns a new list with unique elements of the first list.

my_list = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    my_list.append(ele)

my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)
