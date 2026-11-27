n=int(input("Enter the size of tuple:"))

temp=[]
for i in range(n):
    val=int(input("Numbers enter krr:"))
    temp.append(val)

nums= tuple(temp)

even=[]
odd=[]
for num in nums:
    if(num%2==0):
        even.append(num)
    elif(num%2!=0):
        odd.append(num) 
          
even_tup=tuple(even)
print("Tuple of even numbers", even_tup)
odd_tup=tuple(odd)
print("Tuple of odd numbers",odd_tup)


print(temp)
print(nums)