LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both
numbers are even, but returns the greater if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5

def lesser_of_two_even(a,b):
 if a%2==0 and b%2==0:
  if a<b:
   print (a)
  else:
   print (b)
 else:
  if a>b:
   print (a)
  else:
   print (b)

a = int(input("enter 1 element"))
b = int(input("enter 2 element"))
lesser_of_two_even(a,b)
