#PART C
#COLLABORATORS: Vaibhav, Yoshitha, Sadhana, Ratinakumar, Mourya, Suneethra, Anbu chelvan.
# Take input from user
annual_salary = float(input("Enter the annual salary: "))

# Given fixed values for Part C
total_cost = 1000000              # Cost of the dream house
semi_annual_raise = 0.07          # 7% raise every 6 months
r = 0.04                          # 4% annual return on investment

# Calculate required down payment (25% of total cost)
down_payment = 0.25 * total_cost

# Initialize variables
savings = 0                       # Current savings amount
step = 0                          # Counts number of bisection steps

# Bisection search boundaries (saving rate range from 0 to 1)
low_bound = 0.0
high_bound = 1.0

month = 36                        # We must save within 36 months
found = False                     # To check if solution exists

# Start bisection search
while low_bound <= high_bound:
    
    step += 1                     # Increase step count
    
    # Find middle saving rate
    mid = (low_bound + high_bound) / 2
    rate = mid                    # Current saving rate
    
    savings = 0                   # Reset savings for each trial
    annual_salary_current = annual_salary
    monthly_salary = annual_salary_current / 12

    # Simulate savings for 36 months
    for m in range(1, month + 1):
        
        # Add monthly savings:
        # (1) Interest earned on savings
        # (2) Portion of monthly salary saved
        savings += (savings * r / 12) + (monthly_salary * rate)

        # Apply salary raise every 6 months
        if m % 6 == 0:
            annual_salary_current += annual_salary_current * semi_annual_raise
            monthly_salary = annual_salary_current / 12

    # Check if savings is close enough to down payment (within 100)
    if abs(savings - down_payment) <= 100:
        found = True
        break
    
    # If savings is less than required, increase saving rate
    elif savings < down_payment:
        low_bound = mid
    
    # If savings is more than required, decrease saving rate
    else:
        high_bound = mid

# Print result
if found:
    print("The best saving rate:", round(rate, 4))
    print("The no.of steps in a bisectional search:", step)
else:
    print("It is not possible to pay the down payment in three years")
