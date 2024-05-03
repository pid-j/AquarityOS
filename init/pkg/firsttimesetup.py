import string

valid = string.ascii_letters + string.digits


def Validate(inp: str):
    if len(inp) >= 20:
        return False
    for char in inp:
        if char not in valid:
            return False
    return True


# noinspection PyUnusedLocal
def Main(args):
    personalUsername = input("Username = ")
    if not Validate(personalUsername):
        return "Invalid username."
    personalPasswd = input("Password = ")
    if not Validate(personalPasswd):
        return "Invalid password."
    personalPC = input("Name of PC = ")
    if not Validate(personalPC):
        return "Invalid PC name."
    with open(".auth.txt", "w") as auth:
        auth.write(personalUsername.lower() + "\n")
        auth.write(personalPasswd + "\n")
        auth.write(personalPC)
    return "First-time setup success. Restart shell to see changes"
