import os, subprocess

def decorateMSGBoxes(function):
    def wrapper(*args, **kwargs):
        home = os.getcwd()
        os.chdir("vbs")
        function(*args, **kwargs)
        os.chdir(home)
    return wrapper

@decorateMSGBoxes
def showMSGBox(arg):
    try: subprocess.call(f"cmd /c {arg}.vbs")
    except : subprocess.call(f'wine cscript vbs/{arg}.vbs', shell = True)
