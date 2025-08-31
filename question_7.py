import random as rd

list1 = []
list2 = []

for i in range (40):      #creating the 2 lists randomly

    num = rd.randint(1, 20)
    choice = rd.randint(1, 3)    #if 1, then add to list1, if 2 add to list2, if 3 add to both

    if choice == 1:
        list1.append(num)
    elif choice == 2:
        list2.append(num)
    else:
        list1.append(num)
        list2.append(num)

print("List 1:", list1)
print("List 2:", list2)


finalList = []

for i in list1:
    if (i in list2) and (i not in finalList):   #checking if element is in both lists and not already in finalList
        finalList.append(i)

print("Common elements in both lists :  ", finalList)