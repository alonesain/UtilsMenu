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
[3]-Parad1se Bomber
[4]-HamBom
#PHISHING#
[5]-kingfish
[6]-kingfish2.0
[7]-kingfish3.0
[8]-NexPhisher
#TOOlS#
[9]-Toolss
#DDOS#
[10]-HULK(min 1gb ram)
[11]-Aiohttpdos
#HTTP#
[12]-NGROK or LocalHost.run""")

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
		print(Fore.RED + "Starting Parad1se Bomber")
		os.chdir("Parad1seBomb")
		os.system("python3 main.py")
	elif num == ('4'):
		os.system("clear")
		print(Fore.RED + "Starting HamBom")
		os.chdir("hambom")
		os.system("python3 hambom.py")
	elif num == ('5'):
		os.system("clear")
		print(Fore.CYAN + "Starting kingfish")
		os.chdir("kingfish")
		os.system("python3 fsh.py")
	elif num == ('6'):
		os.system("clear")
		print(Fore.CYAN + "Starting kingfish2.0")
		os.chdir("kingfish2.0")
		os.system("python3 fsh.py")	
	elif num == ('7'):
		os.system("clear")
		print(Fore.CYAN + "Starting kingfish3.0")
		os.chdir("kingfish3.0")
		os.system("python3 fsh.py")
	elif num == ('8'):
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
	elif num == ('9'):
		os.system("clear")
		print(Fore.MAGENTA + "Starting Toolss")
		os.chdir("toolss")
		os.system("python3 Toolss.py")
	elif num == ('10'):
		os.system("clear")
		print(Fore.GREEN + "Starting HULK")
		os.chdir("hulky")
		os.system("python3 hulky.py")
	elif num == ('11'):
		os.system("clear")
		print(Fore.GREEN + "Starting aiohttpdos")
		os.chdir("aiohttpdos")
		os.system("python3 aiohttpdos.py")
	elif num == ('12'):
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


