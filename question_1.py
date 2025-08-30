n = int(input("enter value for n: "))

for i in range (1, n+1):
    for k in range(n-i):
        print("  ", end="")
    for j in range(i):
        print("*", end=" ")
    print()


    