# библиотека для работы сетями
from ipaddress import *

# позволяет преобразовать текст в ip-адрес
ip = ip_address('172.16.128.0')

# создает сеть / все ip-адреса
net = ip_network('172.16.128.0/255.255.192.0')
# или
net = ip_network('172.16.128.0/18')

# перевод в двоичную систему
ip_bin = f'{int(ip):032b}'

# Ip-адрес сети. Зарезервирован, не может быть выдан устройству
network_address = net.network_address

# Широковещательный адрес. Зарезервирован, не может быть выдан устройству
broadcast_address = net.broadcast_address

# Список всех узлов / хостов / ip-адреса устройств в текущей сети
hosts = net.hosts()

# Кол-во ip-адресов включая широковещательный и адрес сети
num_addresses = net.num_addresses

# Маска сети
mask = net.netmask