import os
import time
logo = (" Fuck Bby")
def clear():
	os.system('clear')
clear()
print(logo)
print('Coding By Asraful Islam Hasan')
time.sleep(3.0)
def main():
	clear()
	print(logo)
	print ('(1) (+) ADD ')
	print ('(2) (-) SUBTRACT ')
	print ('(3) (÷) BUG ')
	print ('(4) (×) COUNT ')
	print ('(0) (Exit) Closed ')
	kalibari = input ('Choice Your Option: ')
	if kalibari in '1':
		babi()
		main()
	if kalibari in '2':
		kaki()
		main()
	if kalibari in '3':
		pagli()
		main()
	if kalibari in '4':
		me()
		main()
	if kalibari in '0':
		exit()
# (+) Add 
clear()
print(logo)
clear()
def babi():
	clear()
	asha = input ('Fast  : ')
	asha1 = input ('Secend : ')
	asha = int (asha)
	asha1 = int (asha1)
	print("Your Rusalt=", asha+asha1)
	bbuvai = input ('Entar The Main Menu')
#(-) subtract
clear()
print(logo)
def kaki():
	sumaiya = input ('Fast  : ')
	sumaiya1 = input ('Secend : ')
	sumaiya = int (sumaiya)
	sumaiya1 = int (sumaiya1)
	print("Your Rusalt=", sumaiya-sumaiya1)
	bbuvai = input ('Entar The Main Menu')
# (/) Bug
clear()
print(logo)
def pagli():
	tuki = input ('Fast  : ')
	tuki1 = input ('Secend : ')
	tuki = int (tuki)
	tuki1 = int (tuki1)
	print("Your Rusalt=", tuki/tuki1)
	bbuvai = input ('Entar The Main Menu')
# (×) Count
clear()
print(logo)
def me():
	hasan = input ('Fast  : ')
	hasan1 = input ('Secend : ')
	hasan = int (hasan)
	hasan1 = int (hasan1)
	print("Your Rusalt=", hasan*hasan1)
	bbuvai = input ('Entar The Main Menu')
main()
