from socket import gethostbyname, gethostname
from os import system
from json import dumps

hostname = gethostname()
ip_host = gethostbyname(hostname)

def ping():
    ping_to = ['192.168.0.28', '192.168.0.26', '192.168.0.136', '192.168.0.250']
    availables = []

    reg = open('ip_reg.txt', 'w')
    title = dumps({'locals': {'ip': ip_host, 'host': hostname}}, indent=4)
    reg.write(f'{title}\n\n')

    for ip in ping_to:
        status = system(f'ping -n 2 -w 1 {ip}')
        if status == 0: print(f'{ip} NOT available')
        else:
            availables.append(ip)
            print(f'{ip} AVAILABLE')
    body = str(dumps({'availables': availables}, indent=4))
    reg.write(body)
    reg.close()
    reg = open('ip_reg.txt', 'r')
    print(reg.read())

ping()