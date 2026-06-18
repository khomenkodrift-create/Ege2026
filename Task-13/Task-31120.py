from ipaddress import ip_network

net = ip_network('189.163.226.71/255.255.255.240', False)

print(net.network_address)
print(189 + 163 + 226 + 64)