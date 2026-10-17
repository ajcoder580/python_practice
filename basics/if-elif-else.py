'''Give grades based on marks:
90 or above: Grade A
75 to 89: Grade B
50 to 74: Grade C
Below 50: Fail'''

# marks = int(input("Enter your mark:"))

# if(marks>=90):
#     print("Grabde A")
# elif(marks>=75 and marks<= 89):
#     print("Grade B")
# elif(marks >=50 and marks <=74):
#     print("Grade C")
# else:
#     print("Fail")

'''Find the greatest among three numbers.'''
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if(num1>num2 and num1>num3):
    print("First number is greater")
elif(num2>num1 and num2>num3):
    print("Second number is greater")
elif(num3>num1 and num3>num2):
    print("Third number is greater")
else:
    print("All numbers are equal")