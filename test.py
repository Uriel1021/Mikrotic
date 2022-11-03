"""conectar por SSH el routerOS Mikrotik"""
from netmiko import ConnectHandler
router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '192.168.88.1',
    'username': 'admin',
    'password': 'Unsij2022',
}
#Establecer coneccion con mikrotik
net_connect = ConnectHandler(**router_mikrotik)
#Arreglo de comandos para retornar las interfaces y las direcciones IP
commands =['/interface print',
           '/ip address print',
           '/user print',
           '/interface bridge port print',
           '/ip dhcp-server print',
           '/ip dns print',
           '/ip firewall nat print',
           '/ip route print']
#Crear un archivo para escritura
f = open('mikrotik.txt','w')
#Recorrer el arreglo para posteriormente mostrarlos en pantalla
for commands in commands:
    output = net_connect.send_command(commands, cmd_verify=True)
    print(output)
    #escribir en el archivo de texto
    f.write(output)
    print("\n\n\n")
    f.write("\n\n\n")
#Cerrar el archivo de texto
f.close()