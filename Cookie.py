# Fuck You Baby#


import time
import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
from bs4 import BeautifulSoup as irfan
land = '23860'
hars = '703036'

def irfanx(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0008)

os.system('clear')
print(f""" 
\033[1;34m██████       ██     ███████ ██   ██ ██    ██ ██    ██  ██████      
\033[1;36m██   ██      ██     ██      ██   ██ ██    ██ ██    ██ ██    ██     
\033[1;95m██████       ██     ███████ ███████ ██    ██ ██    ██ ██    ██     
\033[1;33m██   ██ ██   ██          ██ ██   ██ ██    ██  ██  ██  ██    ██     
\033[1;91m██   ██  █████      ███████ ██   ██  ██████    ████    ██████  

\033[1;36m┌──────────────────────────────────────────────────────┐
\033[1;36m│            \033[1;36m[\033[1;91m★\033[1;36m]\033[1;36mUNLIMITED  COOKIE  CLONE  \033[1;91m\033[1;36m[\033[1;91m★\033[1;36m]          │
\033[1;36m└──────────────────────────────────────────────────────┘             
\033[1;36m┌──────────────────────────────────────────────────────┐
\033[1;36m│\033[1;91m[\033[1;36m✓\033[1;91m] \033[1;36mDEVOLPER   :            RJ SHUVO \033[1;36m                 │   
\033[1;36m│\033[1;91m[\033[1;36m✓\033[1;91m] \033[1;36mFACEBOOK   :            RS SHUVO      \033[1;36m            │   
\033[1;36m│\033[1;91m[\033[1;36m✓\033[1;91m] \033[1;36mPAGE       :            RJ COMMANDO  \033[1;36m             │ 
\033[1;36m│\033[1;91m[\033[1;36m✓\033[1;91m] \033[1;36mGITHUB     :            github.com/RJ-Shuvo\033[1;36m       │          
\033[1;36m│\033[1;91m[\033[1;36m✓\033[1;91m] \033[1;36mTOOLS      :            COOKIE    \033[1;91m         \033[1;36m       │ 
\033[1;36m│\033[1;91m[\033[1;36m✓\033[1;91m] \033[1;36mSTATUS     :            FREE \033[1;36m                     │ 
\033[1;36m│\033[1;91m[\033[1;36m✓\033[1;91m] \033[1;36mVERSION    :            2.00 \033[1;36m                     │ 
\033[1;36m└──────────────────────────────────────────────────────┘   """)
os.system('xdg-open https://facebook.com/groups/1396656887527638/')


print('\x1b[92;1m═══════════════════════════════════════════════════════════════')
print()
x = input('[1] Auto Cookie Genaretor \nChoose : ')
ses = requests.Session()
url = irfan(ses.get(f'''https://www.facebook.com/10004{land}28880/posts/6745258{hars}08/?app=fbl''').text, 'html.parser')
data = re.findall('"text":"(.*?)"', str(url))
n = 0
for O in data:
    time.sleep(1)
    n += 1
    irfanx(f'''\x1b[1;93m [{n}] COOKIES💉 : \x1b[1;92m''' + O)
    print()
    
