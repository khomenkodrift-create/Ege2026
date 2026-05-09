from ipaddress import ip_address, ip_network

ip_1 = ip_address('118.187.59.255')
ip_2 = ip_address('118.187.65.115')

for mask in range(10, 31):
    net_1 = ip_network(f'{ip_1}/{mask}', False)
    net_2 = ip_network(f'{ip_2}/{mask}', False)
    if ip_2 in net_2.hosts() and ip_1 in net_1.hosts() and net_1 != net_2:
        print(mask)
        #21
