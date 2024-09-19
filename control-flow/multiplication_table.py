num1 = int(input("Enter a number to see its multiplication table: "))
for num2 in range(1, 11):
    product = num1 * num2
    print(f"{num1} * {num2} = {product}")
    num2 = num2 + 1