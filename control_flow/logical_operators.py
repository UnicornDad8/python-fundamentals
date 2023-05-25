high_income = False
good_credit = True
student = False

# Try with and, or and not
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
print("------------------------------------")

if not student:
    print("Eligible")
else:
    print("Not eligible")
print("------------------------------------")

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
