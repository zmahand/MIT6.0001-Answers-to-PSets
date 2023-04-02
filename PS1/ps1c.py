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
    annual_salary = starting_salary
    monthly_salary = annual_salary / 12
    current_savings = 0

    # Accumulate savings for 36 months
    for month in range(num_of_months):
        current_savings += (monthly_salary * (portion_saved/1000)) + (current_savings * r)
        months += 1
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
    steps += 1
    prev_portion_saved = portion_saved
    if abs(current_savings - down_payment) <= epsilon:
        print(f"Best savings rate: {round(portion_saved/1000, 4)}")
        print(f"Steps in bisection search: {steps}")
        break

    else:
        # Update portion_saved for next loop
        if current_savings < down_payment:
            low = portion_saved
        elif current_savings > down_payment:
            high = portion_saved
        portion_saved = (high + low) / 2
        if portion_saved == prev_portion_saved:
            print("It is not possible to pay the down payment in three years.")
            break
