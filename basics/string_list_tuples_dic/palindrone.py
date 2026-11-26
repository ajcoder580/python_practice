string="apple"
string2=''
for ch in string:
    string2=ch + string2

if(string2==string):
    print("Yes it is a palindrone", string)
else:
    print("Nahh bhai ye string vo nahi jo  soch rahe ho", string)


'''Another way '''
string="level"
string2=''
for i in range(len(string)-1,-1,-1):
    string2+=string[i]

if(string2==string):
    print(" Ha ye wahi hai jo chahiye")
else:
    print("Nahh bhai ye vo nahi hai ")

'''Function to check'''
def str_reverse():
    string=input("Enter a string to check:")
    if string== string[::-1]:
        print("Ha ye vahi string hai")
    else:
        print("Nahi bhai ye o string nahi hai")

str_reverse()