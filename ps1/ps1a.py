# ps1a - House Hunting

# Get Annual Salary
annual_salary = float(input("Enter your annual salary: "))

# Get Savings Contribution (percent as decimal)
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal: "))

# Get Total Cost of House
total_cost = float(input("Enter the cost of your dream home: "))

# Calculate Down Payment (25%)
portion_down_payment = total_cost * 0.25

# Investment Return (Monthly)
r = 0.04 / 12


current_savings = 0
months = 0

while current_savings < portion_down_payment:
    current_savings = current_savings + (current_savings * r)

    current_savings = current_savings + ((annual_salary/12) * portion_saved)

    months = months + 1

print("Number of months", months)
