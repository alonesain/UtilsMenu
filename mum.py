import colorama
from colorama import Fore , Back , Style
import os
import sys

os.system("clear")
print(Fore.RED + "MoreUtilsMenu")
print(Fore.RED + "Author: alonesain")
print(Fore.GREEN + """#BOMBERS#
[1]-b0mb3r
[2]-smsham 
[3]-HamBom
#PHISHING#
[4]-kingfish
[5]-kingfish2.0
[6]-kingfish3.0
[7]-NexPhisher
#TOOlS#
[8]-Toolss
#DDOS#
[9]-Aiohttpdos
#HTTP#
[10]-NGROK or LocalHost.run
Чтобы удалить одну из утилит, пишите перед цифрой утилиты (del). Пример: del 1
To delete one of the utilities, write before the utility number (del). Example: del 1""")

os.chdir('Utilits')

while True:
	num =str(input())
	if num == ('1'):
		os.system("clear")
		print(Fore.RED + "Starting b0mb3r")
		os.system("b0mb3r")
	elif num == ('2'):
		os.system("clear")
		print(Fore.RED + "Starting SmsHam")
		os.chdir("smsham")
		os.system("python3 smsham.py")
	elif num == ('3'):
		os.system("clear")
		print(Fore.RED + "Starting HamBom")
		os.chdir("hambom")
		os.system("python3 hambom.py")
	elif num == ('4'):
		os.system("clear")
		print(Fore.CYAN + "Starting kingfish")
		os.chdir("kingfish")
		os.system("python3 fsh.py")
	elif num == ('5'):
		os.system("clear")
		print(Fore.CYAN + "Starting kingfish2.0")
		os.chdir("kingfish2.0")
		os.system("python3 fsh.py")	
	elif num == ('6'):
		os.system("clear")
		print(Fore.CYAN + "Starting kingfish3.0")
		os.chdir("kingfish3.0")
		os.system("python3 fsh.py")
	elif num == ('7'):
		os.system("clear")
		print(Fore.CYAN + "Starting NexPhisher")
		print(Fore.CYAN + "[1]-Install and start [2]-Start")
		os.chdir("nexphisher")
		nex =str(input())
		if nex == ('1'):
			print(Fore.RED + "[1]-Termux [2]-Linux")
			ter =str(input())
			if ter == ('1'):
				os.system('clear')
				os.system("chmod +x *")
				os.system("./tmux_setup")
				os.system("clear")
				os.system("./nexphisher")
			elif ter == ('2'):
				os.system('clear')
				os.system("chmod +x *")
				os.system("./setup")
				os.system("clear")
				os.system("./nexphisher")
		elif nex == ('2'):
			os.system("bash nexphisher")
	elif num == ('8'):
		os.system("clear")
		print(Fore.MAGENTA + "Starting Toolss")
		os.chdir("toolss")
		os.system("python3 Toolss.py")
	elif num == ('9'):
		os.system("clear")
		print(Fore.GREEN + "Starting aiohttpdos")
		os.chdir("aiohttpdos")
		os.system("python3 aiohttpdos.py")
	elif num == ('10'):
		print(Fore.RED + '[1]-Ngrok [2]-SSH LocalHost')
		http =str(input())
		if http == ('1') :
			os.system("clear")
			print(Fore.RED + "Starting Ngrok")
			print(Fore.RED + "Port?")
			port =str(input())
			os.system("chmod +x *")
			os.system('./ngroka http '+port)
		elif http == ('2') :
			print(Fore.RED + "Starting SSH LocalHost")
			print(Fore.RED + "Port?")
			port =str(input())
			os.system('ssh -R 80:localhost:'+port+' ssh.localhost.run')
	elif num == ('del 1'):
		print(Fore.RED + "Deleting b0mb3r")
		os.system("rm -rf b0mb3r")
		os.system("clear")
		print(Fore.RED + "Deleted")
	elif num == ('del 2'):
		print(Fore.RED + "Deleting smsham")
		os.system("rm -rf b0mb3r")
		os.system("clear")
		print(Fore.RED + "Deleted")
	elif num == ('del 3'):
		print(Fore.RED + "Deleting HamBom")
		os.system("rm -rf HamBom")
		os.system("clear")
		print(Fore.RED + "Deleted")
	elif num == ('del 4'):
		print(Fore.RED + "Deleting kingfish")
		os.system("rm -rf kingfish")
		os.system("clear")
		print(Fore.RED + "Deleted")
	elif num == ('del 5'):
		print(Fore.RED + "Deleting kingfish2")
		os.system("rm -rf kingfish2.0")
		os.system("clear")
		print(Fore.RED + "Deleted")
	elif num == ('del 6'):
		print(Fore.RED + "Deleting kingfish3")
		os.system("rm -rf kingfish3.0")
		os.system("clear")
		print(Fore.RED + "Deleted")
	elif num == ('del 7'):
		print(Fore.RED + "Deleting NexPhisher")
		os.system("rm -rf nexphisher")
		os.system("clear")
		print(Fore.RED + "Deleted")
	elif num == ('del 8'):
		print(Fore.RED + "Deleting Toolss")
		os.system("rm -rf toolss")
		os.system("clear")
		print(Fore.RED + "Deleted")
	elif num == ('del 9'):
		print(Fore.RED + "Deleting aiohttpdos")
		os.system("aiohttpdos")
		os.system("clear")
		print(Fore.RED + "Deleted")
	elif num == ('del 9'):
		print(Fore.RED + "Deleting Ngrok")
		os.system("rm -rf ngroka")
		os.system("clear")
		print(Fore.RED + "Deleted")
