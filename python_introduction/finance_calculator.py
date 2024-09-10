Monthly_savings = int(input("Enter your monthly income: ")) - int(input("Enter your total monthly expenses: "))
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print("Your monthly savings are $" + Monthly_savings)
print("Projected savings after one year, with interest, is: $" + Projected_Savings)
