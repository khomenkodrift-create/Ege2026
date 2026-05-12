from ipaddress import ip_address, ip_network

ip_1 = ip_address('165.112.200.70')
ip_2 = ip_address('165.112.175.80')

for mask in range(10, 31):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_2 in net and ip_1 in net:
        print(mask)