from ipaddress import ip_network

net = ip_network('211.46.0.0/255.255.128.0', False)
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 4 == 0 and ip[-2:] == '11':
        cnt += 1
print(cnt)