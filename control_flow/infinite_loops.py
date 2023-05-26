# with infinite loops remember to always have a way to jump out of the loop
# otherwise your loop will run forever

while True:
    command = input(">")
    print("ECHO", command)

    if command.lower() == "quit":
        break
