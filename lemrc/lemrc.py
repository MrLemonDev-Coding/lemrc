import os

print("Lemrc (still in development.)")

def help():
    cmds = """
    help - Displays this message
    echo <message> - Outputs the message
    mktkui - Creates a tkinter ui (cmd is in testing, cmd may not work)
    """
    print(cmds)

def mainf():
    inp = input("lemrc $> ")
    parts = inp.split(" ", 1)

    if parts[0] == "help":
        help()
    elif parts[0] == "echo" and len(parts) > 1:
        print(parts[1])
    elif parts[0] == "mktkui":
        os.system("python3 cmd/mktkui.py")
    else:
        print(f"Unknown command: {inp} Run 'help' for commands")
    
    mainf()

mainf()
