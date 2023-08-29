import requests
from bs4 import BeautifulSoup

gt = requests.get("https://free-proxy-list.net/")
sp = BeautifulSoup(gt.content, "html.parser")

with open("Files/newestProxy.txt", "a") as f : f.truncate(0)


for i in sp.findAll("textarea", attrs = {"class" : "form-control"}) : 
    with open("Files/newestProxy.txt", "a") as f :
        f.write(str(i))

#
'''
newList = []

with open("newestProxy.txt", "r") as f:
    allElements = f.read().split("\n")
    deleteLines = [0, 1, 2, -1]
    
    for j in allElements : newList.append(allElements[j])
    for i in deleteLines : newList.remove[i]
    
print(newList)
'''