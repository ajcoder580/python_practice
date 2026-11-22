'''Lets create a Simple  
Calculator
calculator(a, b, operation)
that performs arithmetic operations. Create 
a function  that performs addition, subtraction, 
multiplication, or division based on the  parameter.  
operation
[ 
operation + - * /
parameter can have values ,  ,  & .'''

def calculator(a,b,operations):
   if(operations=="+"):
      print(a+b)
   elif(operations=="-"):
      print(a-b)
   elif(operations=="*"):
      print(a*b)
   else:
      print(a/b)

calculator(5,4,"+")