import os
osn = os.name
if os.name == "posix":
    print("NOTICE: You are currently using linux (or macOS) wich is the most supported version for lemrc. Enjoy lemrc.")
elif os.name == "nt":
    print("FATAL WARNING: You are using windows wich is VERY unsupported for lemrc, some commands will not work, to have a more supported version please install an UNIX based OS.")
else:
    print(f"FATAL WARNING: The OS you are currently using (wich is {osn}) is unknown for advice please check if you are using a UNIX based OS if not your on a VERY unsupported OS, some commands will not work, consider installing an UNIX based OS for better support.")

print("Lemrc (still in development.)")

def help():
    cmds = """
    help - Displays this message
    echo <message> - Outputs the message
    mktkui - Creates a tkinter ui (cmd is in testing, cmd may not work)
    ls - Lists the contents of the current directory
    whoami - Shows the current user
    rcasu <command> - runs a command as a superuser (requires admin permissions, only works on UNIX OSs)
    mkfile <name> - Creates a file.
    exit - Exits lemrc.
    """
    print(cmds)

def mainfu():
    inp = input("lemrc $> ")
    parts = inp.split(" ", 1)

    if parts[0] == "help":
        help()
    elif parts[0] == "echo" and len(parts) > 1:
        print(parts[1])
    elif parts[0] == "mktkui":
        os.system("python3 cmd/mktkui.py")

    elif parts[0] == "ls":
        os.system("ls")

    elif parts[0] == "whoami":
        os.system("whoami")

    elif parts[0] == "rcasu" and len(parts) > 1:
        os.system(f"sudo {parts[1]}")

    elif parts[0] == "exit":
        os.system("exit")
    else:
        print(f"Unknown command: {inp} Run 'help' for commands")
    
    mainfu()

mainfu()