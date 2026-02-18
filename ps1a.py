#PART A
# Take user inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Constants
portion_down_payment = 0.25      # 25% of total cost is required as down payment
r = 0.04                         # Annual return on investment (4%)

# Calculate required down payment
down_payment = total_cost * portion_down_payment

# Convert annual salary to monthly salary
monthly_salary = annual_salary / 12

# Convert annual return rate to monthly return rate
monthly_r = r / 12

# Initialize savings amount and month counter
current_savings = 0.0
months = 0

# Loop until savings reach required down payment
while current_savings < down_payment:
    
    # Add monthly savings:
    # (1) Portion of monthly salary saved
    # (2) Interest earned on current savings
    current_savings += (portion_saved * monthly_salary) + (current_savings * monthly_r)
    
    # Increase month count
    months += 1

# Print total number of months required
print("Number of months:", months)
