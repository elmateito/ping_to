def ping():
    ping_to = ['192.168.0.28','192.168.0.26']
    for ip in ping_to:
        status = os.system(f'ping {ip}')
        if status == 0: print(f'{ip} NOT AVAILABLE')
        else: print(f'{ip} AVAILABLE')

ping()
