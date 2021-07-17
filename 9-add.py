list1=[78, 55, 9, 23, 89, 78, 12]
list1.insert(3,99)
print("after insertion:",end="")
for i in range(0,len(list1)):
    print(list1[i],end=" ")
    
print("\r")

list1.remove(12)
print("after deletion:",end="")
for i in range(0,len(list1)):
    print(list1[i],end=" ")
