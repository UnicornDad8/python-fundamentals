successful = True

for number in range(3):
    print("Attenmpt")
    if (successful):
        print("Successful")
        break
print("-------------------------------------------------")

for number in range(3):
    print("Attenmpt")
    if (successful):
        print("Successful")
        break
else:
    print(f"Attempted {number + 1} times and failed")
print("-------------------------------------------------")
