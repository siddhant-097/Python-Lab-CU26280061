# Calculate monthly EMI
principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan tenure in years: "))

monthly_rate = annual_rate / (12 * 100)
months = years * 12

if principal > 0 and years > 0 and annual_rate >= 0:
    if monthly_rate == 0:
        emi = principal / months
    else:
        emi = (
            principal * monthly_rate * (1 + monthly_rate) ** months
        ) / ((1 + monthly_rate) ** months - 1)

    print("Monthly EMI =", round(emi, 2))
else:
    print("Enter valid loan details.")