from ipaddress import ip_address, ip_network

ip = ip_address('218.48.192.56')

for mask in range(10, 33):
    net = ip_network(f'{ip}/{mask}', False)
    if len(list(net.hosts())) >= 500 and net.network_address == ip_address('218.48.192.0'):
        print(net.netmask)
        #6