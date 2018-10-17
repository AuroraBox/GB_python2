import socket
import sys
# port_scaner
host = 'yandex.ru'
# ports = range(2)
ports = [80, 43, 21]
for port in ports:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
    except socket.error:
        print(host, port, 'закрыт')
    else:
        s.close
        # print('{}, : открыт'.format('port'))
        print(host, port, 'открыт')

print('отсканированно - {} порта'.format(len(ports)))
# simple_ports_scaner