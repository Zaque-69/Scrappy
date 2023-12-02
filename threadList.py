import requests

def request(url):
    try:
        return requests.get(url)
    except:
        pass

op = open("Files/com.txt")
hid = []
for i in op:
    hid.append(i.strip())

def multiThreadingDirrs(f, startParam, endParam):
    for line in hid[int(startParam):int(endParam)]:
        response = request(f + line.strip())
        if response:
            try:
                with open("Files/hidden_adr.txt", "a") as file:
                    file.write(f + line.strip())
                    file.write("\n")
            except : pass
