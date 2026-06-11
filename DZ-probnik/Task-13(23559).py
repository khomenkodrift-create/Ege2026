from ipaddress import ip_network
net = ip_network(f'102.162.200.51/255.255.255.0', False)
print(max(net.hosts()))
print(102 + 162 + 200 + 254)