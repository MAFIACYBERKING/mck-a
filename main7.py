version="1.0.1"
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
line=yellow+"-----------------------------------------------------------------------------------------------------------"+end
space=" "
logo=red+str("""
888b     d888  .d8888b.  888    d8P             d8888 
8888b   d8888 d88P  Y88b 888   d8P             d88888 
88888b.d88888 888    888 888  d8P             d88P888 
888Y88888P888 888        888d88K             d88P 888 
888 Y888P 888 888        8888888b   888888  d88P  888 
888  Y8P  888 888    888 888  Y88b  888888 d88P   888 
888   "   888 Y88b  d88P 888   Y88b       d8888888888 
888       888  "Y8888P"  888    Y88b     d88P     888 
                                                      
                                                      
                                                      
""")+end

notice=""
def header():
	print(logo+cyan+"\n\n\n\t\tDeveloped By : MD ALAMIN CHOWDORY\n\n"+green+"\t\t     Version : "+str(version)+" \n\n"+end+line+"\n"+end)
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
r=requests.get('https://pastebin.com/raw/Ga6ej4mA')
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
	notice=cyan+"\t\t[•] Backing up the MCK-A...."
	header()
	os.system("mkdir $HOME/roc-x_updater")
	os.system("cp -rf $HOME/mck-a $HOME/mck-a_updater")
	try:
		clear()
		notice=cyan+"\t\t[•] Updating the Tools...."
		header()
		os.system("cd $HOME")
		os.system("cd $HOME && rm -rf mck-a ")
		print(green)
		os.system("cd $HOME && git clone https://github.com/HANTER2/mck-a")
		
		clear()
		notice=green+"\t\t[√] Update Successful!"
		header()
		#os.kill(os.getppid(), signal.SIGHUP)
		os.system("rm -rf $HOME/mck-a_updater")
		for i in range(99999999999):
			r2=requests.get("https://pastebin.com/raw/Ga6ej4mA")
			r=requests.get('https://pastebin.com/raw/Ga6ej4mA')
			upchck=r.text

			os.system("clear")
			print(green+"\n"*4+"\t  [✓]  Successfully Updated to ROC-X "+yellow+str(upchck)+green+" !\n\n\n\n"+cyan+"  [•] What's New in Version "+str(upchck)+" ?\n\n")
			rng=r2.text
			exec(rng)
			
			a=input()

	except:
		clear()
		notice=red+"\t\t[×] Update Failed!"
		header()
		sjsjstshsb=input(cyan+"\n\n\t     Press Enter to Restore MCK-A")
		os.system("cd $HOME")
		os.system("cd $HOME && mkdir mck-a")
		os.system("cd $HOME && cp -rf $HOME/mck-a_updater/mck-a $HOME")
		os.system("rm -rf $HOME/mck-a_updater")
		os.system("python3 $HOME/mck-a/main.py")
		for i in range(99999999999):
			os.system("clear")
		
#Main Page

while count<2:
	clear()
	header()
	notice=""
	print(cyan+"\n==> Select the number of the option that you want to start from below : ")
	print(yellow+"\n[1] FB CLONE \n\n[2] BD SMS BOMBER(code copy)  \n\n[3] MAIL BOMBER\n\n[4] ENCRYPT/OBFUSCATE SCRIPT \n\n[5] CONTACT ME "+end)
	main_opt=str(input(blue+"\n[>] Select Your Option : "+yellow))
	if main_opt=="1":
		os.system("python fb.py")
		sys.exit()
	
	elif main_opt=="2":
		os.system("python3 bd.py")
	
	elif main_opt=="3":
		os.system("python3 mail.py  ")

	elif main_opt=="4":
		os.system("python3 en.py")

	elif main_opt=="5":
		os.system("os.system('xdg-open https://facebook.com/54321')")
	elif main_opt==str(about):
		os.system('xdg-open https://facebook.com/54321')
		a=input(cyan+"\n\n\t\t[>] Press "+yellow+"Enter"+cyan+" to Continue")
		count=1
	else:
		clear()
		notice=red+"\t\t[×] Wrong Option Entered!"
		count=1