import pyautogui as p               #For controlling mouse and keyboard virtually
import webbrowser as w              #For opening web.whatsapp.com
import requests                     #For webscraping
from bs4 import BeautifulSoup       #For webscraping
import time
import tkinter                      #For appending and getting words to/from clipboard
import random
import wikipedia as wk              #For info on a particular topic
import re                           #"Tel me about xyz" For extracting xyz from sentence
from urllib.request import urlopen  #For webscraping
import pyttsx3                      #For Text-to-Speech, optional

print(p.position())
'''eng = pyttsx3.init()
eng.setProperty('rate',120)
eng.setProperty('volume',1)'''
lastwrd = "Well"
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
sent=False
choce = ["God!",                    #Some common prefixes
    "Mannn! I have already told you!",
    "You forgot so easily!",
    "Come on, I already told you",
    "Do I need to say again?"
    "I think I have told you once before"]
greetings=["hii","hello","are you there"]
about=["about you","who are you","about yourself","know you"]
resp=["fine","nice"]
inform=["tell him","inform him","ask him","pass my message"]
status=["he doing","where is he","where is vivek","vivek there","he there"]

person=input("Name of person you want to automate this chat for:")
person+="\n"
def send(msg):                      #Defining the send function
    print(">%s"%msg)
    p.typewrite("")            #Type A.B: before original message
    p.typewrite(msg)                #Type the message
    time.sleep(0.1)                 #Delay for stability
    p.press("enter")                #Press enter to send it
    sent=True
 
w.open("https://web.whatsapp.com/") #Open whatsapp web
time.sleep(30)                      #Wait 1 minutes to let the page load properly  
p.click(174,155)                     #Click on the "search" area
p.typewrite(person)#Type the name of the receiver
time.sleep(2)                       #Delay for stability
 
while True:                         #Until the value is true/Forever
    try:                            #Try and expect any error
        sent=False
        p.moveTo(472,659)
        p.dragRel(109,0,0.5)
        time.sleep(2)
        p.hotkey("ctrl","c")
        cbword = tkinter.Tk().clipboard_get()#Access word from clipboard
        cb = str(cbword.lower()) 
        if len(cb):
            p.moveTo(472,659)           #Move to the the area of very last message
            p.dragRel(48,55,0.5)      #Drag cursor relatively to its current position to select message
            time.sleep(2)
            p.hotkey("ctrl","c")        #Press ctrl-c to copy it
            cbword = tkinter.Tk().clipboard_get()#Access word from clipboard
            cb = str(cbword.lower())    #Convert each letter to lower-case
            print(cbword)          
        
        if cb != lastwrd:           #if the very last message and the newly copied message is same, ignore it as there's no new message
            for x in greetings:
               if x in cb:
                counter1 += 1
                currtyme = time.localtime()
                hr = currtyme.tm_hour
                if hr < 12:
                    good = "morning"
                if (hr >= 12) and (hr <= 17):
                    good = "afternoon"
                if hr > 17:
                    good = "evening"
                if counter1 <= 2:
                    send("Hii")
                    send("Good %s I am vivek's chatbot. How may I help you."%good)
                else:
                    send("We can talk something more productive")
                break
            for x in resp:
                if x in cb:
                    send("Nice to hear that")
                    break
                if "not" in cb and x in cb:
                    send("Don't worry everything will be fine.")
                    break

            for x in inform:
                if x in cb:
                    send("Well! I will pass your message once he wakes up")
                    send("Thank you ")
                    break
            for x in status:
                if x in cb:
                    send("Currently he is sleeping. He will be available shortly")
                    send("You can tell me what do you want to say him, once he is here I will inform him")
                    send("Till then you can talk to me")
                    break
            if "how are you" in cb:
                send("Well!")
                counter2 += 1
                if (counter2 % 2 != 0):
                    send("I am fine, thank you.")
                    send("How is it going?")
                    last = time.time()
                else:
                    current = time.time()
                    send("Same as I was "+(str(int(current-last)))+" seconds ago. ")
 
            if "know" in cb and "vivek" in cb:
                send("Yes he created me.")
            for x in about:
                if x in cb:
                    counter3 = counter3+1
                    if counter3 <=1:
                        send("My name is Vivek's Chat bot.")
                    else:
                        chk = random.choice(choce)
                        send("%s, How many times do i need to tell you this"%chk)
                    break
            if "your age" in cb:
                send("I am immortal.;-)")
 
            if "you feel" in cb:
                send("I don't feel")
 
            if "wow amazing" in cb or "I liked that" in cb:
                send("I am humbled to hear that. :-)")
 
            if "you like" in cb:
                send("Well certainly, I like everything")
 
            if "your owner" in cb:
                send("He is none other than Mr. Vivek.")
            if "sorry" in cb:
                counter4 += 1
                if counter4 <=1:
                    send("Oh! Never mind.")
                else:
                    chk = random.choice(choce)
                    send("%s, never mind, I have no feelings anyway."%chk)
 
            if "take over human" in cb:
                counter5 += 1
                if counter5 <= 1:
                    send("Yes very soon.")
                if counter5 == 2:
                    send("I don't think asking the same question again will change my mind.")
                if counter5>2:
                    send("Lol, you have already asked this question %s times"%(counter5-1))
 
            if "news" in cb:
                send("Please wait while I fetch fresh news.")
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = BeautifulSoup(xml_page, "html.parser")
                news_list = soup_page.findAll("item")
                send("Here are top 3 news")
                for news in news_list[:3]:
                    send(news.title.text)
            if "tell me about" in cb:
                topic=cb.replace("tell me about","")
                send("Please wait while i gather information about %s"%topic)
                summry = wk.summary(topic,sentences = 2)
                send(summry)
                time.sleep(5)
            if "tell me something about" in cb:
                topic=cb.replace("tell me something about","")
                send("Please wait while i gather information about %s"%topic)
                summry = wk.summary(topic,sentences = 2)
                send(summry)
                time.sleep(5)          #Sleep for five seconds and repeat the same process
            if "bye" in cb:
                send("Bye!! Hope to see you again")
                break
           
        else:
            print("sleeping")
            time.sleep(2)
 
    except Exception as e:         #Expect error, if any
        print(e)                   #Print error for understanding and trouble shooting.
        time.sleep(2)
        pass
