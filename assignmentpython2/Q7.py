#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
#extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
#summer_69([1, 3, 5]) --> 9
#summer_69([4, 5, 6, 7, 8, 9]) --> 9
#summer_69([2, 1, 6, 9, 11]) --> 14


def sumexcludingrange(list): 
	sum = 0
	add = True
	for i in range(len(list)): 
		if list[i] != 6 and add == True: 
			sum=sum+list[i] 
		elif list[i] == 6: 
			add=False
		elif list[i] == 9: 
			add = True
	print (sum)

arr=[]
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input())
    arr.append(ele)
sumexcludingrange(arr) 
