annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

monthly_salary = annual_salary / 12
R = 0.04
portion_down_payment = total_cost * 0.25
current_savings = 0
number_of_months = 0

while current_savings < portion_down_payment:
    current_savings += (monthly_salary * portion_saved) + (current_savings * R / 12)
    number_of_months += 1

print(f"Number of months: {number_of_months}")