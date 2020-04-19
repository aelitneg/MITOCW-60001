# ps1c Finding the right amount to save away

# Get Annual Salary
annual_salary = float(input("Enter your annual salary: "))

# Set Values
semi_annual_raise = 0.07    # Semi-Annual Raise

r = 0.04 / 12               # Investment Return

total_cost = 1000000        # Total Cost of House

savings_term = 36           # Months of Saving

# Calculate Down Payment
portion_down_payment = total_cost * 0.25

# Initialize Bisection Search Variables
current_savings = 0
min_pct = 0
max_pct = 10000
steps = 0

# Perform Bisection Search
while (abs(current_savings - portion_down_payment) > 100):
    # Reset Bisection Search Variables
    current_savings = 0

    # Find Midpoint Search Value
    pct = (min_pct + max_pct) // 2

    # Calculate Savings After 36 Months
    current_annual_salary = annual_salary
    semi_annual_count = 0
    for month in range(36):
        # Handle Semi-Annual Raise
        if (semi_annual_count == 6):
            current_annual_salary = current_annual_salary + \
                current_annual_salary * semi_annual_raise
            semi_annual_count = 0

        # Add Investment Income
        current_savings = current_savings + current_savings * r

        # Add Savings Contribution
        current_savings = current_savings + \
            current_annual_salary / 12 * (pct/10000)

        # Increment Semi-Annual Counter
        semi_annual_count = semi_annual_count + 1

    # Set Bounds for Next Search Iteration
    if current_savings > portion_down_payment:
        max_pct = pct
    else:
        min_pct = pct

    if (max_pct + min_pct) // 2 == pct:
        pct = 0
        break

    # Increment search steps
    steps = steps + 1

if not pct:
    print("It is not possible to pay the down payment in 3 years.")
else:
    print("Best savings rate:", pct/10000)
    print("Search Steps:", steps)
