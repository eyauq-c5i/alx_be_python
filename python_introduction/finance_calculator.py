monthly_income = float(input("Enter your monthly income: $"))

monthly_expenses = float(input("Enter your total monthly expenses: $"))

monthly_savings = monthly_income - monthly_expenses

annual_interest_rate = 0.05

total_monthly_savings_for_year = monthly_savings * 12

interest_earned = total_monthly_savings_for_year * annual_interest_rate

projected_annual_savings = total_monthly_savings_for_year + interest_earned


print(f"\nYour monthly savings are: ${monthly_savings:.2f}")

print(f"Your projected savings after one year, including 5% interest, will be: ${projected_annual_savings:.2f}")