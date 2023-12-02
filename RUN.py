import subprocess, platform
from threading import Thread

truncFiles = ["Files/newestProxy.txt", "Files/validPr.txt"]

opSys = platform.system()

def deleteFileData(e):
    with open(f"{e}", "a") as f : 
        f.truncate(0)

for j in truncFiles : Thread(target = deleteFileData(j)).start()

if ( opSys == 'Linux'):
    def file1():  subprocess.call("python scraping.py")
    def file2():  subprocess.call("python validateProxy.py")

else :
    def file1():  subprocess.call("cmd /c scraping.py", shell = True)
    def file2():  subprocess.call("cmd /c validateProxy.py", shell = True)

Thread(target = file1).start()
Thread(target = file2).start()
