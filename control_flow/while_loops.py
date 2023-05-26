number = 100

while number > 0:
    print(number)
    number //= 2
print("-----------------------------------------------------")

command = ""

while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
