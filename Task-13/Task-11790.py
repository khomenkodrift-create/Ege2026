from ipaddress import ip_network
def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('0') >= ip[16:].count('0')

for mask in range(16, 25):
    net = ip_network(f'152.65.245.132/{mask}', False)
    if all(f(ip) for ip in net):
        print(net.netmask)