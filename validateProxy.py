import requests, threading, queue, subprocess, sys

q = queue.Queue()

try : subprocess.call("cmd /c getProxy.py")
except : subprocess.call("python3 getProxy.py", shell = True)

with open("Files/newestProxy.txt", "r") as f : 
    proxies = f.read().split("\n")
    for p in proxies: q.put(p)

myIp = requests.get("https://ipinfo.io/json").json()['ip']

count = 0

def chechProxies():
    global q, count
    
    while not q.empty():
        proxy = q.get()

        try:
            res = requests.get("https://ipinfo.io/json", 
                proxies = {
                    "http" : proxy, "https" : proxy
                }
            )
        except : continue

        if res.status_code == 200:
            with open("Files/validPr.txt", "a") as newFile : 
                newFile.write(str(proxy) + '\n')
            count += 1
        if count == 3 : return 
        
for _ in range(1000) : threading.Thread( target = chechProxies ).start()
