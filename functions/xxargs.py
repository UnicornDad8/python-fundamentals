# In this case **user variable is a dictionary

def save_user(**user):
    print(user["name"])


save_user(id=1, name="Ceci", age=30)
