from ipaddress import ip_network

net = ip_network('172.16.96.0/255.255.224.0')
cnt = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 2 ==0:
        cnt+=1
print(cnt)