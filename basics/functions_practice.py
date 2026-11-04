# ==============================================
# Python Functions Practice
# ==============================================
# How to use:
#   1. Replace `pass` in each function with your own code.
#   2. Run the file (Run button, or in terminal: python functions_practice.py)
#   3. Each question shows PASS or FAIL at the bottom.
# Tip: solve one question at a time, run, fix, then move on.


# ---------- Level 1: Basics ----------

def cube(n):
    """Return the cube of n. cube(3) -> 27"""
    return n**3


def is_odd(n):
    """Return True if n is odd, else False."""
    if(n%2!=0):
      return "true"
    else:
        return "False"


def add(a, b=10):
    """Return a + b. If b is not given, use 10. add(5) -> 15"""
    return a+b



# ---------- Level 2: Conditions ----------

def smallest(a, b, c):
    """Return the smallest of three numbers WITHOUT using min()."""
    if(a>b and c>b):
        return b
    elif(b>a and c>a):
        return a
    else:
        return c


def grade(marks):
    """90+ -> 'A', 75-89 -> 'B', 50-74 -> 'C', below 50 -> 'Fail'"""
    if(marks>=90):
        return 'A'
    elif(marks>78 and marks<89):
        return 'B'
    elif(marks>=50 and marks<74):
        return 'C'
    else:
        return 'Fail'

    


# ---------- Level 3: Loops inside functions ----------

def count_even(numbers):
    """Return how many even numbers are in the list."""
    count=0
    for i in range(0, len(numbers)):
        if(i%2==0):
            count+=1
    return count
    


def factorial(n):
    """Return n! using a loop. factorial(5) -> 120, factorial(0) -> 1"""
    factorial=1
    for i in range(1, n+1):
       factorial=factorial*i
    return factorial      
    


def is_prime(n):
    """Return True if n is prime, else False. (1 is not prime)"""
    for i in range(2,n+1):
        if(n%i==0):
            return "false"
        
        elif(n%1==0):
            return "true"
    


def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in text. Ignore case."""
    count=0
    for ch in text.lower():
        count+=1 if ch in ("a", "e", "i","o","u") else 0

    return count
        


def reverse_string(s):
    """Return the reversed string. Try it with a loop first."""
    result = ""
    for ch in s:
        result = ch + result
    return result
        
    


def is_palindrome(s):
    """Return True if the string reads the same backwards."""
    is_palindrome="false"
    result = ""
    for ch in s:
        result = ch + result
        if(result==s):
            is_palindrome="true"
    return is_palindrome



# ---------- Level 4: Return values, *args, recursion ----------

def min_max(numbers):
    """Return (smallest, largest) of a list. Do not use min()/max()."""
    pass


def average(*nums):
    """Return the average of any number of values. average(2, 4, 6) -> 4.0"""
    pass


def power_sum(n):
    """Return 1**1 + 2**2 + ... + n**n. power_sum(3) -> 32"""
    pass


def sum_digits(n):
    """Return the sum of digits using RECURSION. sum_digits(1234) -> 10"""
    pass


def grade_report(marks_list):
    """Return a dict with keys: total, average, highest, lowest."""
    pass


# ==============================================
# Tests (do not edit below this line)
# ==============================================

def check(name, got, expected):
    status = "PASS" if got == expected else "FAIL"
    print(f"[{status}] {name}: got {got!r}, expected {expected!r}")


def run(name, func, args, expected):
    try:
        got = func(*args)
    except Exception as e:
        got = f"Error: {e}"
    check(f"{name}{args}", got, expected)


print("--- Level 1 ---")
run("cube", cube, (3,), 27)
run("cube", cube, (-2,), -8)
run("is_odd", is_odd, (7,), True)
run("is_odd", is_odd, (10,), False)
run("add", add, (5,), 15)
run("add", add, (5, 20), 25)

print("--- Level 2 ---")
run("smallest", smallest, (4, 2, 9), 2)
run("smallest", smallest, (7, 7, 3), 3)
run("grade", grade, (95,), "A")
run("grade", grade, (80,), "B")
run("grade", grade, (50,), "C")
run("grade", grade, (49,), "Fail")

print("--- Level 3 ---")
run("count_even", count_even, ([1, 2, 3, 4, 6],), 3)
run("factorial", factorial, (5,), 120)
run("factorial", factorial, (0,), 1)
run("is_prime", is_prime, (17,), True)
run("is_prime", is_prime, (15,), False)
run("is_prime", is_prime, (1,), False)
run("count_vowels", count_vowels, ("Education",), 5)
run("reverse_string", reverse_string, ("python",), "nohtyp")
run("is_palindrome", is_palindrome, ("madam",), True)
run("is_palindrome", is_palindrome, ("hello",), False)

print("--- Level 4 ---")
run("min_max", min_max, ([4, 9, 1, 7],), (1, 9))
run("average", average, (2, 4, 6), 4.0)
run("power_sum", power_sum, (3,), 32)
run("power_sum", power_sum, (1,), 1)
run("sum_digits", sum_digits, (1234,), 10)
run("grade_report", grade_report, ([80, 90, 70],),
    {"total": 240, "average": 80.0, "highest": 90, "lowest": 70})
