annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
r = 0.04

down_payment = portion_down_payment * total_cost
monthly_salary = annual_salary / 12
monthly_r = r / 12

current_savings = 0.0
months = 0

while current_savings < down_payment:
    current_savings += (portion_saved * monthly_salary) + (current_savings * monthly_r)
    months += 1

print("Number of months:", months)
