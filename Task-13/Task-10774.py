from ipaddress import ip_network

net = ip_network('217.19.128.131/255.255.192.0', False)

print(net.network_address)
#HCEA