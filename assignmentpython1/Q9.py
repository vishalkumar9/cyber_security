#Write a program to print N fibonacci numbers where N is being passed from command line and you
#can run python program using command - python fibo.py 20, where N=20.


import sys
def Fibonacci(n):
    n1, n2, count = 0, 1, 0
    if n < 0:
        print("Please enter a positive integer")
    elif n == 1:
        print("Fibonacci sequence upto",n,":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
n=int (sys.argv[1])  
Fibonacci(n)
