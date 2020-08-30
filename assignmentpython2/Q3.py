#Given a sentence, return a sentence with the words reversed
#reversed_words('I am home') --> 'home am I’
#reversed_words('We are ready') --> 'ready are We’
#Note: The .join() method may be useful here. The .join() method allows you to join together
#strings in a list with some connector string. For example, some uses of the .join() method:

def rev_sentence(sentence): 
    words = sentence.split(' ')  
    reverse_sentence = ' '.join(reversed(words))  
    return reverse_sentence   
str=input("enter your string")    
print(rev_sentence(str))
