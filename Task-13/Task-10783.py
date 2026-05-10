from ipaddress import ip_network, ip_address

ip_1 = ip_address('121.171.5.70')
ip_2 = ip_address('121.171.5.107')

for mask in range(10, 31):
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net and ip_2 in net:
        print(net.num_addresses)
        #64