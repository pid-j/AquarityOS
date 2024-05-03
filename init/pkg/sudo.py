global authenticated
# noinspection PyRedeclaration
authenticated = False


def Main(args):
    global authenticated
    if len(args) < 1:
        return "Syntax error: sudo takes in arguments"
    command = args[0]
    params = args[1::1]
    # noinspection PyUnresolvedReferences
    from commands import CommandList as commands
    if commands.Has(command):
        if not authenticated:
            password = ""
            with open(".auth.txt") as auth:
                password = auth.readlines()[1]
            ask = input("Password of current user = ")
            if ask != password.strip():
                return "Authentication failed."
            authenticated = True
        result = commands.Get(command).callback(params)
        return result
    return "Syntax error: No command found named %s" % command
