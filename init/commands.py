from pkg import *


class Command:
    def __init__(self, name: str, callback):
        self.name = name
        self.callback = callback


class Commands:
    def __init__(self, commands: list):
        self.commands = commands

    def Has(self, commandName: str) -> bool:
        for command in self.commands:
            if command.name == commandName:
                return True
        return False

    def Get(self, commandName: str):
        for command in self.commands:
            if command.name == commandName:
                return command
        return None


def Echo(args: list):
    return " ".join(args)


CommandList = Commands(
    [
        Command("echo", echocmd.Main),
        Command("fetchdist", fetchdist.Main),
        Command("clr", clear.Main),
        Command("exit", lambda args: exit()),
        Command("help", helpcmd.Main),
        Command("ftsetup", firsttimesetup.Main),
        Command("sudo", sudo.Main)
    ]
)
