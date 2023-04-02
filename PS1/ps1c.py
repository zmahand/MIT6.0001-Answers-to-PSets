starting_salary = float(input("Enter the starting salary: "))

# Initialize variables
epsilon = 100                       # Allowed margin of error
semi_annual_raise = 0.07            # percent salary increase every 6 months
r = 0.04 / 12                       # monthly return on investments
down_payment = 1000000*.25          # Down payment is 25% of $1M house price
current_savings = 0                 # initial savings
num_of_months = 36                  # total period of saving
high = 10000                        # Max savings rate, 100%
low = 0                             # Min savings rate, 0%
portion_saved = (high + low) / 2    # Start bisection variable
months = 1                          # Increment for semi-annual raise
steps = 0

while True:
    # Reset variables
    portion_saved = (high + low) / 2
    annual_salary = starting_salary
    current_savings = 0

    # Accumulate savings for 36 months
    for month in range(0, num_of_months):
        monthly_salary = annual_salary / 12
        current_savings += (monthly_salary * (portion_saved/10000)) + (current_savings * r)
        months += 1
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    if abs(current_savings - down_payment) <= epsilon:
        print(f"Best savings rate: {round(portion_saved/10000, 4)}")
        print(f"Steps in bisection search: {steps}")
        break

    elif abs(current_savings - down_payment) > epsilon and current_savings > down_payment:
        high = portion_saved

    elif abs(current_savings - down_payment) > epsilon and current_savings < down_payment:
        low = portion_saved

    if low == high:
        print('It is not possible to pay the down payment in three years.')
        break

    steps = steps + 1