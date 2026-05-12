from ipaddress import ip_address, ip_network
ip_1 = ip_address('157.127.172.56')
ip_2 = ip_address('157.127.191.78')

for mask in range(10, 31):
    net_1 = ip_network(f'{ip_1}/{mask}', False)
    net_2 = ip_network(f'{ip_2}/{mask}', False)
    if ip_1 in net_1.hosts() and ip_2 in net_2.hosts() and net_1 != net_2:
        print(mask)
        break
        #20