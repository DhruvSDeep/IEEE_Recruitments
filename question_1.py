n = int(input("enter value for n: "))

for i in range (1, n+1):
    for k in range(n-i):      #adding the spaces, equalling n-i
        print("  ", end="")
    for j in range(i):        #adding the stars, equalling i
        print("*", end=" ")
    print()                   #to seperate rows into different lines


    