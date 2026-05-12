from ipaddress import ip_network
net = ip_network(f'143.168.72.213/255.255.255.240', False)
print(max(net.hosts()))