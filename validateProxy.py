import requests, threading, queue, subprocess, sys

q = queue.Queue()

subprocess.call("cmd /c getProxy.py")

with open("Files/newestProxy.txt", "r") as f : 
    proxies = f.read().split("\n")
    for p in proxies: q.put(p)

myIp = requests.get("https://ipinfo.io/json").json()['ip']

count = 0

def chechProxies():
    global q, count
    
    while not q.empty():
        proxy = q.get()
        #print("start")
        try:
            res = requests.get("https://ipinfo.io/json", 
                proxies = {
                    "http" : proxy, "https" : proxy
                }
            )
        except : continue
        if res.status_code == 200:

            with open("Files/validPr.txt", "a") as newFile : 
                newFile.write(str(proxy))
                newFile.write("\n")
            
            count += 1

        if count == 3 : return 
 
        
for _ in range(1000) : threading.Thread( target = chechProxies ).start()

#print("FILE 2 FINISHED")
#C:\Users\zamfi\OneDrive\Desktop

#https://ipinfo.io/json
#https://jsonip.com/