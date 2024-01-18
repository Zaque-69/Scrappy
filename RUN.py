import subprocess
from threading import Thread

truncFiles = ["Files/newestProxy.txt", "Files/validPr.txt"]

def deleteFileData(e):
    with open(f"{e}", "a") as f : 
        f.truncate(0)

for j in truncFiles : Thread(target = deleteFileData(j)).start()

def file1():  subprocess.call("python3 scraping.py",  shell = True)
def file2():  subprocess.call("python3 validateProxy.py",  shell = True)

Thread(target = file1).start()
Thread(target = file2).start()
