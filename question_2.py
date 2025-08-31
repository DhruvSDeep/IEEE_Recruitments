para = input("Enter a paragraph: ").split()

noneCheck = False    #to check if no palindrome is found

for i in para:
    if i == i[::-1]:    #checking if the word is a palindrome
        print(i)
        noneCheck = True   #ensuring noneCheck is True when a palindrome is found

if noneCheck == False:   #printing 0 if no palindrome is found
    print("0")