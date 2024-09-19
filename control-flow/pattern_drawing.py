dor = int(input("Enter the size of the pattern: "))
go = dor
while dor >= 1:
    for x in range(1, go + 1):
        print("*", end="")
    dor = dor - 1
    print()  