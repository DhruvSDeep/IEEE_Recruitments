para = input("Enter a paragraph: ").split()
noneCheck = False
for i in para:
    if i == i[::-1]:
        print(i)
        noneCheck = True

if noneCheck == False:
    print("0")