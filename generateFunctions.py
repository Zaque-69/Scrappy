'''
this python file is gonna create some functions that are insert in another python file
the functions will be thread:

def example(f):
    for line in hid[x:y]: ---> interval 
        response = request(f + line.strip())
        if response:
            with open("Files/hidden_adr.in", "a") as file:
                file.write(f + line.strip())
                file.write("\\n")
'''
import random
fil = open("threadList.py", "a")
fil.truncate(0)
fil.close()
print("started generatefunctions")
with open("threadList.py", "a") as file:

    string = "abcdefghijklmnopqrstuvwxyz"
    listOfFunctions = []

    minNr = 1
    maximNr = 11

    file.write("""import requests
from threading import Thread

def request(url):
    try:
        return requests.get(url)
    except:
        pass

op = open("Files/com.txt")
hid = []
for i in op:
    hid.append(i.strip())
""")
    file.write("\n")

    for i in range(10):
        randomString  = "".join(random.sample(string, k = 5))
        file.write("def " + str(randomString) + "(f):" + "\n")
        file.write("    for line in hid[" + str(minNr) + ":" + str(maximNr) + "]:" + "\n")
        file.write("""        response = request(f + line.strip())
        if response:

            with open("Files/hidden_adr.txt", "a") as file:
                file.write(f + line.strip())
                file.write("\\n")""" + "\n" )
        listOfFunctions.append(randomString)
        minNr += 15
        maximNr += 15
    file.write("\n")
    file.write("def finalThread(par):" + "\n")
    for j in listOfFunctions:
        file.write("    Thread(target = "+ str(j) + "(par)).start()" + "\n")
        
    #print(listOfFunctions)