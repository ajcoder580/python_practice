#printing number from 1 to 10
print("Printing 1 to 10")
for i in range(1,11):
    print(i)

#Printing number from 10 to 1 in reverse order
print("printing 10 to 1")
for i in range(10, 0,-1):
    print(i)

# Printing all even numbers form 1 to 50
print("printing all even number form 1 to 50")
for i in range(1,51):
    if(i%2==0):
        print(i)

# Printing all odd numbers form 1 to 50
print("printing all odd number form 1 to 50")
for i in range(1,51):
    if(i%2!=0):
        print(i)
    
#printing table of 5
for i in range(1, 11):
    print(i*5)

#printing square of number from 1 to 10
for i in range(1,11):
    print(i**2)


#printing cube of numbers from 1 to 10
for i in range(1,11):
    print(i**3)

#printing name 
for i in range(1,21):
    print("Hi Buddy")

'''printing table from 1 to 10'''
for i in range(1,11):
    for j in range(1,11):
        print(i*j)

'''Printing Sum of number from 1 to 100'''
sum=0
for i in range(101):
    print("Printing sum of ", i,""+"",sum)
    sum=i+sum
    print(sum)

'''Printing sum of even numbers from 1 to 100'''
sum = 0
for i in range(1,101):
    if(i%2==0):
        print("Printing sum of ", i ,"" + "", sum)
        sum=i+sum
        print(sum)

'''Count how many numbers between 1 and 100 are divisible by 7.'''
count=0
for i in range(1,101):
    if i % 7==0:
        print(i)
        count+=1

print("Total numbers divisible by 7 = ",count)

'''Calculate the factorial of a number entered by the user.'''
num = int(input("Factorial ke liye number enter kar: "))

fact=1
for i in range(1,num+1):
    fact=fact*i
    print(fact)

'''Count how many vowels are present in a given string.'''
s = "visualization"
count = 0
for i in s:
    if i in "aeiou":
        count+=1
print(count)

'''Find the sum of the digits of a number using a for loop.'''
digit = 8794
total=0
for i in str(digit):
    total = total + int(i)   
print(total)

'''Print all numbers between 1 and 100 that are divisible by both 3 and 5.'''
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i)

'''Check whether a number is prime.'''
n = int(input("Enter any number: "))
is_prime = True        

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break          

print(is_prime)

'''Print all prime numbers from 1 to 100.'''
for i in range(1,101):
    if(i%2!=0 and i%i!=0 and i%1!=0):
        print(i)