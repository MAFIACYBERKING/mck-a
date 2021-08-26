version="2.3.6"
#IMPORT
import getpass,time,os,sys
import signal
import time,os,sys
import sys, random
import threading,time
#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
black="\033[0;30m"
N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
P="\033[0;35m"
Y = '\033[1;33m'
C = '\033[1;36m'

logo=(R+"""
888b     d888  .d8888b.  888    d8P             d8888 
8888b   d8888 d88P  Y88b 888   d8P             d88888 
88888b.d88888 888    888 888  d8P             d88P888 
888Y88888P888 888        888d88K             d88P 888 
888 Y888P 888 888        8888888b   888888  d88P  888 
888  Y8P  888 888    888 888  Y88b  888888 d88P   888 
888   "   888 Y88b  d88P 888   Y88b       d8888888888 
888       888  "Y8888P"  888    Y88b     d88P     888 
                                                      
                                                      
                                                      
""")
line=("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
def header():
	print(logo+cyan+"\n\n\n\t\tDeveloped By : MD ALAMIN CHOWDOWRY \n\n"+C+"\t\t     Version : "+str(version)+" \n\n"+end+line+"\n"+end)
def clear():
        os.system("clear || cls")
count=1
erase = '\x1b[1A\x1b[2K'
count=1
about=12

os.system("clear")
header()
print(cyan+"\n\t\t[•] Checking For Updates")
time.sleep(0.7)


try:
	import requests
except:
	os.system("pip install requests")
import requests
r=requests.get('https://pastebin.com/raw/8mVewP9W')
upchck=r.text
if upchck==version:
	pass
elif upchck!=version:
	os.system("clear")
	header()
	print(cyan+"\n  [°] Installing The Updated Tools. Allow Up to 10 minutes ")
	time.sleep(2)
	os.system("clear")
	notice=cyan+"\t\t[°] Installing Updated Tools.. \n"
	header()
	notice=""
	print("\n")
	clear()
	notice=cyan+"\t\t[•] Backing up the mck-a...."
	header()
	os.system("mkdir $HOME/mck-a_updater")
	os.system("cp -rf $HOME/mck-a $HOME/mck-a_updater")
	try:
		clear()
		notice=cyan+"\t\t[•] Updating the Tools...."
		header()
		os.system("cd $HOME")
		os.system("cd $HOME && rm -rf mck-a-x")
		print(green)
		os.system("cd $HOME && https://github.com/HANTER2/mck-a")
		
		clear()
		notice=green+"\t\t[√] Update Successful!"
		header()
		#os.kill(os.getppid(), signal.SIGHUP)
		os.system("rm -rf $HOME/mck-a_updater")
		for i in range(99999999999):
			r2=requests.get("https://pastebin.com/raw/6sBnXFV7")
			r=requests.get('https://pastebin.com/raw/8mVewP9W')
			upchck=r.text

			os.system("clear")
			print(green+"\n"*4+"\t  [✓]  Successfully Updated to ROC-X "+yellow+str(upchck)+green+" !\n\n\n\n"+cyan+"  [•] What's New in Version "+str(upchck)+" ?\n\n")
			rng=r2.text
			exec(rng)
			print(yellow+"\n\n\n [•••] TerMux Restart is Required for The Update. Please Restart Termux For The ROC-X Updated Version")
			a=input()

	except:
		clear()
		notice=red+"\t\t[×] Update Failed!"
		header()
		sjsjstshsb=input(cyan+"\n\n\t     Press Enter to Restore ROC-X")
		os.system("cd $HOME")
		os.system("cd $HOME && mkdir mck-a ")
		os.system("cd $HOME && cp -rf $HOME/mck-a_updater/mck-a $HOME")
		os.system("rm -rf $HOME/mck-a_updater")
		os.system("python3 $HOME/mck-a/main.py")
		for i in range(99999999999):
			os.system("clear")
			a=input(cyan+"\n"*10+" [>] Please Exit Termux from Notification Bar. Then Again Open ROC-X Tools By :\n\n "+yellow+"\t [1] Exit Termux\n\t [2] Open Termux"+"\n\t [3] cd $HOME/roc-x"+yellow+"\n\t [4] "+yellow+"python3 main.py\n\n")
		
#Main Page

while count<2:
	clear()
	header()
	notice=""
def manu():
     choose=input(Y+"\n\nEnter Your Option :"+B+" ")
     while True:
            		if choose=="1":
            			os.system("clear")
            			os.system("python fb.py ")
            			a=input(C+"Do You Went main manu prass y enter: ")
            			os.system("clear")
            			manu()
            		if choose=="2":
            			os.system("clear")
            			os.system("python bd.py")
            			
            			a=input(C+"Do You Went main manu prass y enter: ")
            			os.system("clear")
            			manu()
            		if choose=="3":
            			os.system("clear")
            			os.system("python mail.py")
            			a=input(C+"Do You Went main manu prass y enter: ")
            			os.system("clear")
            			os.system("clear")
            			manu()
            		if choose=="4":
            			os.system("clear")
            			os.system("python en.py")
            			a=input(C+"Do You Went main manu prass y enter: ")
            			os.system("clear")
            			manu()
            		if choose=="5":
            			  os.system("clear")
            			  os.system('xdg-open https://facebook.com/54321')
            			  time.sleep(6)
            			  os.system("clear")
            			  manu()
            		else:
            		 	print(" 1 press for fb clone 2 press  for BD SMS Bomber\n 3 press for Mail Bomber 4 press for python code Encrypt\n 5 press for Contact me ")
            		 	time.sleep(10)
            		 	os.system("clear")
            		 	manu()
            			
            		
            		
            		
               
               
manu()