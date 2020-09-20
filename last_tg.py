import os
dir_log = '/var/log/pi-star/'
log_files=os.walk(dir_log)
lista= list(log_files)[0]
arquivo=lista[2][0]
i=1
while not arquivo.startswith('MMDVM'):
        arquivo=lista[2][i]
        i=i+1
#last_log=lista[0]+lista[2][0]
last_log=lista[0]+arquivo

print(last_log)
file=open(last_log,'r')
content=file.readlines()
ultima_linha=content[-1]
i=-1
try:
        while not 'to TG' in ultima_linha:
                i=i-1
                ultima_linha=content[i]
except:
        pass

print(ultima_linha)
if 'to TG' in ultima_linha:
        text=ultima_linha.split('to TG')
        last_tg=text[1].split(',')[0]
        if last_tg.startswith(' '):
                last_tg=last_tg[1:]
        if last_tg.endswith('\n'):
                last_tg=last_tg[:-1]
        command='sudo pistar-bmapi deltg %s 0'%(last_tg)
        print(command)
        os.system('sudo pistar-bmapi dropqso 0')
        os.system(command)
