# ps1b - Saving, with a raise

# Get Annual Salary
annual_salary = float(input("Enter your annual salary: "))

# Get Savings Contribution (percent as decimal)
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal: "))

# Get Total Cost of House
total_cost = float(input("Enter the cost of your dream home: "))

# Get the Semi-Annual Raise (percent as a decimal)
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Calculate Down Payment (25%)
portion_down_payment = total_cost * 0.25

# Investment Return (Monthly)
r = 0.04 / 12


current_savings = 0
months = 0
semi_annual_months = 0
while current_savings < portion_down_payment:
    if (semi_annual_months == 6):
        annual_salary = annual_salary + (annual_salary * semi_annual_raise)
        semi_annual_months = 0

    current_savings = current_savings + (current_savings * r)

    current_savings = current_savings + ((annual_salary/12) * portion_saved)

    months = months + 1
    semi_annual_months = semi_annual_months + 1

print("Number of months", months)
