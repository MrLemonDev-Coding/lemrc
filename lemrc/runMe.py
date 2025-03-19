import os
import subprocess
import sys

def install_libraries():
    try:
        subprocess.check_call(["pip", "install", "tkinter"])
    except subprocess.CalledProcessError:
        print("Failed to install tkinter using pip.")

    print("Libary already installed.")

def check_and_install():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        install_libraries()
    except FileNotFoundError:
        print("Python or pip is not installed or not found.")
        print("To troubleshoot: 1) Install Python3 2) Install pip 3) Reinstall Python3 and pip if needed.")
    except subprocess.CalledProcessError:
        print("There was an error running pip.")
        print("To troubleshoot: 1) Make sure pip is installed correctly.")

check_and_install()
