#Write a function that checks whether a number is in a given range (inclusive of high and low).

def test_range(n):
  l=int(input("enter low value"))
  h=int(input("enter high value"))
    if n in range(l,h):
        print( "in the range")
    else :
        print("outside the given range")
        
n=int(input("enter the number"))
test_range(n)
