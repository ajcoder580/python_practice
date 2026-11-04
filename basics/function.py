#Function with no parameter and no return
def greet():
    print("Hello")

greet()
#Function with parameter but no return
def greet1(name):
    print("Hello", name)

greet1("Rahul")

#with parameters and retunrs
def square(n):
    return n*n

print(square(9))

#default agrgument
def power(base, exp=2):
    return base ** exp

print(power(7))


def show(a, b=10):
       print(a + b)

print(show(5))
print(show(5, 20))

# def reverse_string(s):
#     result = ""
#     for ch in s:
#         result = ch + result
#         print(result)
#     return result

# print(reverse_string("python"))   # nohtyp

'''Check whether the string is Palindrome or not'''
def is_Palindrome(s):
    answer = False
    result=""
    for ch in s:
        result = ch + result
    if(result==s):
        answer=True
        print(answer)

    print(result)
    return answer

is_Palindrome("hello")