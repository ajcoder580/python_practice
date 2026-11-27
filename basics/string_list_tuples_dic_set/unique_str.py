string = input("Enter any string:")

seen=set()
for ch in string:
    seen.add(ch)

print("Unique characters of string",seen)
print("Count of unique char",len(seen))