#Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their
#sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after
#adjustment) exceeds 21, return ‘BUST’.
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

def check_sum(a,b,c):
    sum1=a+b+c
    if a != 11 and b != 11 and c != 11:
        if sum1 > 21:
            print("BUST")
        else:
            print(sum1)    
    else:
        print (sum1-10)

a=int(input("enter 1 number: "))
b=int(input("enter 2 number: "))
c=int(input("enter 3 number: "))
check_sum(a,b,c)
