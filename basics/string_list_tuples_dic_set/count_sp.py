string = input("Enter any string:")
count=0
for ch in string:
    if(ch==" "):
        count+=1
print("Space in string\n",count)