import os
import subprocess

def succes():
    home = os.getcwd()
    os.chdir("vbs")
    subprocess.call("cmd /c succes.vbs")
    os.chdir(home)

def searchError():
    home = os.getcwd()
    os.chdir("vbs")
    subprocess.call("cmd /c searchError.vbs")
    os.chdir(home)

def expiredProxy():
    home = os.getcwd()
    os.chdir("vbs")
    subprocess.call("cmd /c expiredProxy.vbs")
    os.chdir(home)