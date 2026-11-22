''' Write a function  
prime(n)
True n
that returns  if  is a prime number and 
False

otherwise, using a loop.'''

def is_prime(num):
 
 if num<2:
   return False
 for i in range(2,num):
    if(num%i==0):
     return False
    else:
     return True


print(is_prime(50))