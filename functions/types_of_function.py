'''
There are two types of function, a function that:
1- Performs a task
2- Returns a value
'''


def task_greeting(name):  # This function is consider a task since it returns None...
    print(f"Hi {name}")


def get_greeting(name):  # This returns the string "Hi Ceci"
    return f"Hi {name}"


print(get_greeting("Ceci"))
print(task_greeting("Paz"))
