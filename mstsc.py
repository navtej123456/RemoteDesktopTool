import os 
import time
import socket

os.system('color 02')

print(r'''  
    _   __            __         _ _____ _             __  
   / | / /___ __   __/ /____    (_) ___/(_)___  ____ _/ /_ 
  /  |/ / __ `/ | / / __/ _ \  / /\__ \/ / __ \/ __ `/ __ \
 / /|  / /_/ /| |/ / /_/  __/ / /___/ / / / / / /_/ / / / /
/_/ |_/\__,_/ |___/\__/\___/_/ //____/_/_/ /_/\__, /_/ /_/ 
                          /___/              /____/        ''')

ip=input('Enter IP Address >> ')

os.system('cls')

os.system("color 04")

print(r''' 
    __  __           __   _             ________      __  
   / / / /___ ______/ /__(_)___  ____ _/ ____/ /_  __/ /_ 
  / /_/ / __ `/ ___/ //_/ / __ \/ __ `/ /   / / / / / __ \
 / __  / /_/ / /__/ ,< / / / / / /_/ / /___/ / /_/ / /_/ /
/_/ /_/\__,_/\___/_/|_/_/_/ /_/\__, /\____/_/\__,_/_.___/ 
                              /____/
''')

print(f'*************NavtejSinghClub***********************')

def check_connection(host="www.google.com", port=80, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.create_connection((host, port))
        return True
    except socket.error:
        return False

if check_connection():
    print("Network statue.....")
    
    time.sleep(1)
    os.system('cls')
    print(r''' 
    __  __           __   _             ________      __  
   / / / /___ ______/ /__(_)___  ____ _/ ____/ /_  __/ /_ 
  / /_/ / __ `/ ___/ //_/ / __ \/ __ `/ /   / / / / / __ \
 / __  / /_/ / /__/ ,< / / / / / /_/ / /___/ / /_/ / /_/ /
/_/ /_/\__,_/\___/_/|_/_/_/ /_/\__, /\____/_/\__,_/_.___/ 
                              /____/
''')

    print(f'*************NavtejSinghClub***********************')
    print('Network statue.....Online')

    time.sleep(1)

    cammand = ("mstsc /v:"+ip)

    os.system(cammand)
else:
    print("Network statue.....")
    time.sleep(1)
    os.system('cls')
    print(r''' 
    __  __           __   _             ________      __  
   / / / /___ ______/ /__(_)___  ____ _/ ____/ /_  __/ /_ 
  / /_/ / __ `/ ___/ //_/ / __ \/ __ `/ /   / / / / / __ \
 / __  / /_/ / /__/ ,< / / / / / /_/ / /___/ / /_/ / /_/ /
/_/ /_/\__,_/\___/_/|_/_/_/ /_/\__, /\____/_/\__,_/_.___/ 
                              /____/
''')

    print(f'*************NavtejSinghClub***********************')
    print('Network statue.....Offline')

    