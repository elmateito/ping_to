from socket import gethostbyname, gethostname, gethostbyaddr
from os import system
from json import dumps
from time import time

hostname = gethostname()
ip_host = gethostbyname(hostname)

def mk_txt(ip_host, hostname, availables, assigned, failed):
    reg = open('ip_reg.txt', 'w')
    content = {'result': {'locals': {'ip': ip_host, 'host': hostname},
                'availables': availables,
                'assigned': assigned,
                'failed': failed}}
    body = dumps(content, indent=4)
    reg.write(body)
    reg.close()
    reg = open('ip_reg.txt', 'r')
    return reg.read()

def ping():
    timer = time()
    availables, assigned, failed = [], [], []
    for i in range(0, 17): #iter from 192.168.0.0 to 192.168.0.8
        ip = f'192.168.0.{i}'
        try:
            status = system(f'ping -n 2 -w 1 {ip}')
            if status == 0: assigned.append({ip: gethostbyaddr(ip)[0]})
            else: availables.append(ip)  
        except: 
            failed.append(ip)
            print(f'\n{ip}: ping failed')
        file = mk_txt(ip_host, hostname, availables, assigned, failed) 
    print(f'{file}\n--- execution time: %s secs ---\n' % (round((time() - timer), 3)))

ping()