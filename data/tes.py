import marshal, os, time

logo = ('''
  __  __                _           _ 
 |  \/  |              | |         | |
 | \  / | __ _ _ __ ___| |__   __ _| |
 | |\/| |/ _` | '__/ __| '_ \ / _` | |
 | |  | | (_| | |  \__ \ | | | (_| | |
 |_|  |_|\__,_|_|  |___/_| |_|\__,_|_|
''')

os.system('clear')
print (logo)

def main():
    try:
        a = input('(+) Masukan File : ')
        x = open(a).read()
        b = compile(x, '<code>', 'exec')
        c = a.replace('.py', '_enc.py')
        d = marshal.dumps(b)
        e = open(c, 'w')
        e.write('# Compile by Pahrul\n# Github : https://github.com/P4HRUL\n\n')
        e.write('import marshal\n')
        e.write('exec(marshal.loads(' + repr(d) + '))')
        e.close()
        time.sleep(2)
        print('\n(+) Selesai...')
        exit()
    except IOError:
        print('\n(+) File Tidak Ditemukan !!!')
        exit()
    except KeyboardInterrupt:
        exit()


main()
