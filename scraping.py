import os, re, shutil, requests,  webbrowser, customtkinter, random, json

from tkinter import *
from threading import Thread
from bs4 import BeautifulSoup  
from urllib.parse import urljoin

#local modules
from messagebox import showMSGBox
from colored import bcolors, decorations

home = os.getcwd()

os.chdir(home)
class scrap:
    def __init__(self, master):
        self.master = master
        
        #labels
        Label(master, bg="#363047", text="Web Scraping", font=(14), fg="white").place(x = 150, y = 30)
        Label(master, text="Please insert your link:", bg="#363047", fg="white").place(x = 50, y = 70)
        Label(master, bg="#363047", text = "").pack()
        Label(master, text="Status Code :", bg="#363047", fg="white").place(x = 725, y = 155)
        Label(master, bg="#363047", text="© 2023 Z4que ALL RIGHTS RESERVED", fg="white").place(x=20, y=390)
        Label(master, bg="#363047", text="URLs Found", fg="white", font=(14)).place(x=530, y = 30)
        Label(master, bg="#363047", text="Hidden Pages", fg="white", font=(14)).place(x=140, y = 230)
        Label(master, bg="#363047", text="Proxy Info", fg="white", font=(14)).place(x=540, y = 230)
        Label(master, bg="#363047", text="E-mails Found", fg="white", font=(14)).place(x=775, y=30)
        Label(master, bg="#363047", text="User Agent", fg="white", font=(14)).place(x=790, y=230)

        #entries 
        self.inputtxt = customtkinter.CTkEntry(master, placeholder_text="https://www.example.com/", width=300, height=25, border_width=2, corner_radius=5, fg_color = "#0E0C12", text_color = "white",border_color="#000")
        self.name = customtkinter.CTkEntry(master, placeholder_text="Name (optional)", width=300, height=25, border_width=2, corner_radius=5, fg_color = "#0E0C12", text_color = "white", border_color="#000")
        self.search = customtkinter.CTkEntry(master, placeholder_text="Search", width=300, height=25, border_width=2, corner_radius=5, fg_color = "#0E0C12", text_color = "white",border_color="#000")
        self.st = customtkinter.CTkEntry(master, placeholder_text="XXX", width=130, height=25, border_width=2, corner_radius=5, fg_color = "#191621", text_color = "#80C148", border_color="#0E0C12")
        self.totalFiles = customtkinter.CTkEntry(master, width=220, height=25, border_width=2, corner_radius=5, fg_color = "#191621", text_color = "#968BC4", border_color="#0E0C12") 

        self.choseYourIp = customtkinter.CTkEntry(master, placeholder_text="255.0.0.0:PORT", width=160, height=25, border_width=2, corner_radius=5, fg_color = "#0E0C12", text_color = "#D69044", border_color="#000")
        self.currentIp = customtkinter.CTkEntry(master, placeholder_text="Your IP", width=220, height=25, border_width=2, corner_radius=5, fg_color = "#191621", text_color = "#D69044", border_color="#0E0C12")
        self.changedIp = customtkinter.CTkEntry(master, placeholder_text="Changed IP", width=220, height=25, border_width=2, corner_radius=5, fg_color = "#191621", text_color = "#D69044", border_color="#0E0C12") 


        #findHidden
        self.inputtxt.place(x = 50, y = 100)
        self.name.place(x = 50, y = 140)
        self.search.place(x = 50, y = 180)
        self.st.place(x = 815, y = 155)
        self.totalFiles.place(x = 475, y = 180) 

        self.choseYourIp.place(x = 475, y = 267)
        self.changedIp.place(x = 475, y = 307)
        self.currentIp.place(x = 475, y = 347) 

        #buttosn
        customtkinter.CTkButton(master, width=60, height=60, text="Run", fg_color="#574E73", hover_color="#706494", text_color="black", border_width=1, corner_radius=5, border_color="#4B4363", command = self.main).place(x = 380, y = 100)
        customtkinter.CTkButton(master, width=60, height=40, text="Find", fg_color="#574E73", hover_color="#706494", text_color="black", border_width=1, corner_radius=5, border_color="#4B4363", command = self.threadFindHidden).place(x = 380, y = 270)
        customtkinter.CTkButton(master, width=60, height=40, text="Reload", fg_color="#574E73", hover_color="#706494", text_color="black", border_width=1, corner_radius=5, border_color="#4B4363", command = self.reload).place(x = 380, y = 330)
        customtkinter.CTkButton(master, width=60, height=30, text="Search", fg_color="#574E73", hover_color="#706494", text_color="black", border_width=1, corner_radius=5, border_color="#4B4363", command = self.searchLink).place(x = 380, y = 177.5)
        customtkinter.CTkButton(master, width=30, height=30, text="Servers", fg_color="#574E73", hover_color="#706494", text_color="black", border_width=1, corner_radius=5, border_color="#4B4363", command = self.openservers).place(x = 645, y = 263.5)

        #text areas
        self.output = customtkinter.CTkTextbox(master , width=300, height=100, border_width=2, corner_radius=5, fg_color = "#191621", text_color = "#8D8B93", border_color="#0E0C12")
        self.domains = customtkinter.CTkTextbox(master, width=220, height=80, border_width=2, corner_radius=5, fg_color = "#191621", text_color = "#E7CF50", border_color="#0E0C12")
        self.afis = customtkinter.CTkTextbox(master , width=220, height=100, border_width=2, corner_radius=5, fg_color = "#191621", text_color = "#D0669F", border_color="#0E0C12")
        self.yourUserAgent = customtkinter.CTkEntry(master, placeholder_text="Your User Agent (optional)", width=220, height=25, border_width=2, corner_radius=5, fg_color = "#191621", text_color = "#D0669F", border_color="#0E0C12")
        self.userAgent = customtkinter.CTkTextbox(master, width=220, height=70, border_width=2, corner_radius=5, fg_color = "#191621", text_color = "#74CFC1", border_color="#0E0C12")

        self.output.place(x = 50, y = 270)
        self.afis.place(x = 475, y = 70)
        self.domains.place(x = 725, y = 70)
        self.yourUserAgent.place(x = 725, y = 265)
        self.userAgent.place(x = 725, y = 300)

        self.phtotExtensions = ["jpeg", "jpg", "png", "gif", 
                               "tiff", "psd", "pdf", "eps", "ai"]
        
        self.need2Delete = ['output', 'changedIp', 'currentIp', 'st',
                             'userAgent' 'afis', 'domains', 'totalFiles']

        with open("Files/hidden_adr.txt", "w") as nush: pass

    def openservers(self) : 
        os.system('Files\ValidPr.txt')

    def searchLink(self):
        SEARCH = self.search.get()
        if str(SEARCH[:8]) == "https://" : return webbrowser.open_new(str(SEARCH))
        else : return showMSGBox('searchError')

    def reload(self):
        self.output.delete("1.0", END)
        for j in open("Files/hidden_adr.txt", "r"): self.output.insert(END, j, "\n")

    def main(self):

        #deleting the text from inputs and textareas

        self.currentIp.delete(0, 'end')
        self.changedIp.delete(0, 'end')
        self.st.delete(0, 'end')
        self.totalFiles.delete(0, 'end')

        self.userAgent.delete('1.0', END)
        self.domains.delete('1.0', END)
        self.output.delete('1.0', END)

        #with open("threadList.py",'a') as file: file.truncate(0)

        finalName, aux = '', ''
        INPUT = self.inputtxt.get()
        NAME = self.name.get()
        if len(NAME) == 0:

            if "https://www." in INPUT : aux = INPUT.replace(INPUT[:12], "")
            else : aux = INPUT.replace(INPUT[:8], "")

            for char in aux :
                if char == "." : break
                finalName += str(char)

        else: finalName = NAME
        os.mkdir(str(finalName) + "_Folder")
        
        def refresh(self):
            self.output.delete("1.0", END)
            for j in open("Files/hidden_adr.txt", "r"): self.output.insert(END, j)

        def sec():
            
            global home
            os.chdir(home)
            #subprocess.call("cmd /c generateFunctions.py")
            
        def getimgName(word):
            fin = ''
            for char in word[::-1] : 
                fin += char
                if char == "/" : return fin[:int(len(fin)-1)][::-1]

        def scr(self):
            global home
            self.afis.delete("1.0", END)

            if (self.yourUserAgent.get()) : randomValue = self.yourUserAgent.get()
            else : randomValue = random.choice(open('Files/ua.txt').readlines()).split('\n')[0]

            randomValidProxy = ''

#                    #starting scraping
            try:
                randomValidProxy = self.choseYourIp.get()

                gt = requests.get(str(INPUT), headers = {
                    "User-Agent" : randomValue 
                        },
                        proxies = {
                            "http" : randomValidProxy, 
                            "https" : randomValidProxy
                        }
                    )
                print(bcolors.HEADER + 'EXIT STATUS CODE : ' + decorations.BOLD + bcolors.LIGHT_RED + f'{gt.raise_for_status} ' + decorations.ENDC)
                sp = BeautifulSoup(gt.content, "html.parser")

                getInfoOldIp = requests.get("https://ipinfo.io/json")

                getInfoNewIp = requests.get("https://ipinfo.io/json", proxies = {
                    "http" : randomValidProxy, "https" : randomValidProxy
                    })
                
                print(bcolors.LIGHT_CYAN + 'CHANGED INFO : ')
                for key, value in json.loads(getInfoNewIp.text).items() : 
                    print(bcolors.OKBLUE + 8*' ' + f'[{key.upper()}] : ' + decorations.ENDC , bcolors.OKCYAN + f'{value}' + decorations.ENDC)

                mainAtts = ['ip', 'country', 'region']
                
                self.changedIp.insert(END, "Changed Information : ")
                self.currentIp.insert(END, "Your Information : ")

                for i in mainAtts : self.changedIp.insert(END, str(getInfoNewIp.json()[i]) + " ")
                for i in mainAtts : self.currentIp.insert(END, str(getInfoOldIp.json()[i]) + " ")

            except : 
                
                for i in self.need2Delete : 
                    try : self.i.delete('1.0', END)
                    except : pass
                with open('Files/hidden_adr.txt', 'a') as f : f.truncate(0)
                showMSGBox('searchError')
                return

            self.st.insert(END, gt.status_code)
            self.userAgent.insert(END, randomValue)

            for i in self.phtotExtensions:

                if i in str(INPUT[-5:]):
                    with open(getimgName(INPUT), "wb") as file : 
                        file.write(gt.content)
                        return

            with open("HtmlCodeContent.html", "a", encoding = 'utf-8') as f: f.write(str(gt.content))
            with open("HtmlCodeText.html", "a", encoding = 'utf-8') as f: f.write(str(gt.text))
                    
            def scraping(self, var, source, elements): 

                if not os.path.exists(elements): 
                    print(bcolors.WARNING + '🗀 CREATED FOLDER : ' + decorations.BOLD + 
                          bcolors.YELLOW + str(elements) + decorations.ENDC, '\n', 4 * ' ' + 
                          bcolors.OKGREEN + f'Moving files to {str(elements)}' + decorations.ENDC)
                    os.mkdir(elements)

                for i in sp.find_all(var):
                    try:
                        name = os.path.basename(i[source])           
                        url = urljoin(INPUT, i.get(source))
                        path = os.path.join(elements, name)
                        self.afis.insert(END, "URL FOUNFD : " + str(url) + "\n" + "\n", )
                    
                        if not os.path.isfile(path):
                            with open(path, 'wb') as file:
                                filebin = requests.Session().get(url)
                                file.write(filebin.content)
                    except :
                        pass
            
            alt = ["img", "video", "iframe", "source", "audio"]
            hr = ["a", "link", "area", "base"]

            for i in alt : scraping(self, var = i, source = "src", elements = "media_files")
            for j in hr : scraping(self, var = j, source = "href", elements = "hypertext_files")

            scraping(self, var = "script", source = "src", elements = "script_files")
            scraping(self, var = "img", source = "data-src", elements = "media_files")

        def findEmails(self):

            global emails
        
            gt = requests.get(str(INPUT))
            sp = BeautifulSoup(gt.content, "html.parser")

            email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
            emails = email_regex.findall(sp.prettify())
            emails += email_regex.findall(sp.text)

            for j in set(emails)  : self.domains.insert(END, str(j) + "\n")

        #activate functions
        Thread(target = sec).start()
        scr(self)
        refresh(self)
        findEmails(self)
 
        filesDownloaded = 0

        for file in os.listdir():

            if file == "media_files" or file == "script_files" or file == "hypertext_files":
                os.chdir(file)

                for document in os.listdir(): filesDownloaded += 1
                os.chdir(home)
                shutil.move(file, str(finalName) + "_Folder")

            elif file == "HtmlCodeContent.html" or file == "HtmlCodeText.html":
                shutil.move(file, str(finalName) + "_Folder")
                
        self.totalFiles.insert(END, f"Total files downloaded : {filesDownloaded}. + HTML code")

        os.chdir(home)
        showMSGBox('succes')

    def findHidden(self):
        self.output.delete("1.0", END)
        start, end = 0, 10
        from threadList import multiThreadingDirrs

        for i in range(10):
            try: 
                Thread(target = multiThreadingDirrs(str(self.inputtxt.get()), start, end)).start()
                start += 10
                end += 10 
            except : pass
        
    def threadFindHidden(self): Thread(target = self.findHidden).start()

root = Tk()
root.geometry("975x420")
root.configure(bg="#363047")
root.config(cursor = "top_left_arrow")
root.wm_attributes('-toolwindow', 'True')
root.resizable(False, False)
root.title("Web Scraping")

ah = scrap(root)
        
if __name__ == "__main__": root.mainloop()
