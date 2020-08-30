#Write a function that returns the number of prime numbers that exist up to and including a given
#number. Hint - By convention, 0 and 1 are not prime.
#count_primes(100) --> 25


def countPrimes(n):
      count = 0
      primes = [False for i in range(n+1)]
      for i in range(2,n+1):
         if primes[i] == False:
            count+=1
            j = 2
            while j*i<n+1:
               primes[j*i] = True
               j+=1
      return count
n=int(input("enter range"))
print(countPrimes(n))      
