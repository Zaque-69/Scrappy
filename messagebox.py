import os, subprocess

def showMSGBox(arg):
    subprocess.call(f"chmod +x shell/{arg}.sh", shell = True)
    subprocess.call(f"sh shell/{arg}.sh", shell = True)
