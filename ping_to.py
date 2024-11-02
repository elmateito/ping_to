from socket import gethostbyname, gethostname, gethostbyaddr
from os import system
from json import dumps

hostname = gethostname()
ip_host = gethostbyname(hostname)

def mk_txt(ip_host, hostname, availables, assigned):
    reg = open('ip_reg.txt', 'w')
    content = {'result': {'locals': {'ip': ip_host, 'host': hostname},
                'availables': availables,
                'assigned': assigned}}
    body = dumps(content, indent=4)
    reg.write(body)
    reg.close()
    reg = open('ip_reg.txt', 'r')

def ping():
    availables = []
    assigned = []
    for i in range(1, 16):
        try:
            ip = f'192.168.0.{i}'
            status = system(f'ping -n 2 -w 1 {ip}')
            if status == 0: assigned.append({ip: gethostbyaddr(ip)[0]})
            else: availables.append(ip)
            mk_txt(ip_host, hostname, availables, assigned)
        except: 
            print('conn failed')

ping()