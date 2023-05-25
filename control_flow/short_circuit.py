high_income = True  # Try with True and False
good_credit = True
student = False

if high_income and good_credit and not student:
    print("Eligible")
print("--------------------------------------------------")

if high_income or good_credit or not student:
    print("Eligible")
