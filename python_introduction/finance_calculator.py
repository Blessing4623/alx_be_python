Monthly_income = int(input("Enter your monthly income: "))
Monthly_expenses = int(input("Enter your total monthly expenses: "))
Monthly_savings = Monthly_income - Monthly_expenses
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print("Your monthly savings are $" + Monthly_savings)
print("Projected savings after one year, with interest, is: $" + Projected_Savings)
