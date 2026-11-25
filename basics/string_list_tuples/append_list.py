l1 = int(input("Enter the length of first list: "))
list1 = []
for i in range(l1):
    list1.append(input("Enter a value: "))

l2 = int(input("Enter the length of second list: "))
list2 = []
for i in range(l2):
    list2.append(input("Enter a value: "))

list1.extend(list2)      # or: merged = list1 + list2
print("Merged list:", list1)