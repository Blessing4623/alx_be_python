number = int(input("Enter a number to see its multiplication table: "))
for num2 in range(1, 11):
    product = number * num2
    print(f"{number} * {num2} = {product}")
    num2 = num2 + 1