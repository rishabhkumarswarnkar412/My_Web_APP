l1=int(input('enter lentgh of list1'))
l2=int(input('enter lentgh of list2'))
list1=[]
list2=[]
for i in range(l1):
    list1.append(int(input("enter elements for list1: ")))
    
for i in range(l2):
    list2.append(int(input("enter elements for list2: "))) 
print(list1)
print(list2)
for i in list1:
    for j in list2:
        if i==j:
            list1.remove(i)
            list2.remove(j)
        else:
            pass
print(list1)