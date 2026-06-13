from ipaddress import ip_network, ip_address

ip1 = ip_address('157.127.182.76')
ip2 = ip_address('157.127.190.80')

for mask in range(10, 33):
    net_1 = ip_network(f'{ip1}/{mask}', False)
    net_2 = ip_network(f'{ip2}/{mask}', False)
    if ip1 in net_1.hosts() and ip2 in net_2.hosts() and net_1 != net_2:
        print(mask)
