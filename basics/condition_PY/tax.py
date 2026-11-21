#Program to calculate tax on salary
salary=float(input("Enter Your Salary"))

tax=0
if(salary<30000):
   tax= salary*0.05
elif(salary>30000 and salary<70000):
   tax=salary*0.15
elif(salary>70000):
   tax=salary*0.25

print(tax)

'''Write a function that takes two integers  and  and prints all even 
numbers between them (inclusive).'''
def even_btn(a,b):
    for num in range(a,b+1):
       if num%2==0:
        print(num)
    

even_btn(10,20)

'''Write a function that prints the  digits n of a number.'''

def print_dgt(n):
   dgt=0
   while (n>0):
      dgt=n%10
      print(dgt)
      n=n//10


print_dgt(312)

'''Write a function to count digit in a number, n'''

def count_dgt(n):
   count=0
   while(n>0):
      n=n//10
      count+=1
   return count

print(count_dgt(3565))

'''Write a function to return sum of digit of a number'''
def sum_dgt(n):
   sum=0
   while(n>0):
      sum=sum + (n%10)
      n=n//10
   return sum

print(sum_dgt(456))