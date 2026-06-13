from ipaddress import ip_address, ip_network

ip1 = ip_address('193.175.175.231')
ip2 = ip_address('193.175.176.118')

for mask in range(10, 33):
    net_1 = ip_network(f'{ip1}/{mask}', False)
    net_2 = ip_network(f'{ip2}/{mask}', False)
    if ip1 in net_1.hosts() and ip2 in net_2.hosts() and net_1 != net_2:
        print(net_1.netmask)
        #240