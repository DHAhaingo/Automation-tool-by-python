# from curses import newwin
# from distutils.command.config import config
# from sqlite3 import getpass
from netmiko import ConnectHandler
import msvcrt as m
import getpass


#----------------------------------------------------------------------------------------------------------------------------------------#
#CHECK IP
#----------------------------------------------------------------------------------------------------------------------------------------#
def checkIP(ip):
    octet= ip.split('.')    # split ip into 4 octet ex:192.168.1.1 => [192,168,1,1]
    if len(octet) == 4:
        for i in range(4):
            if octet[i] < '0' or octet[i] > '255' or octet == '':
                return False
            else: return True
    else: return False

#----------------------------------------------------------------------------------------------------------------------------------------#
#Enter infor of device
#----------------------------------------------------------------------------------------------------------------------------------------#

ip_dev = input('enter ip of device: ')
username = input('enter username: ')
password = input('enter password: ')
if checkIP(ip_dev) == True:
    info_dev = {
        'device_type':'cisco_ios',
        'host': ip_dev,
        'username': username,
        'password': password,
        'secret':'123456@A',
    }
    print('Connect sucessful!!!\n')
else:
    print('Username or password is wrong. Please enter again')
net_connect = ConnectHandler(**info_dev)
print(net_connect.find_prompt())

#----------------------------------------------------------------------------------------------------------------------------------------#
#Information of device
#----------------------------------------------------------------------------------------------------------------------------------------#

def info_device():
    net_connect= ConnectHandler(**info_dev)
    print("\t\n Information of device\n")
    print(net_connect.send_command('show arp'))
    print("\t\n Ports status\n")
    print(net_connect.send_command('show ip interface brief'))

    dev_name = str(net_connect.find_prompt())
    if dev_name[0] == 'R':
        print("\t\n Routing table\n")
        print(net_connect.send_command('show ip route'))
    else:
        print("\t\n VLAN\n")
        print(net_connect.send_command('show vlan'))


#----------------------------------------------------------------------------------------------------------------------------------------#
#Interface Configuration
#----------------------------------------------------------------------------------------------------------------------------------------#

def interface_config():
    net_connect = ConnectHandler(**info_dev)
    dict_int = {}
    while True:
        end = input('Enter to continue or end to finish.\n')
        if end != 'end':
            int = input("Interface:\t")
            ip_int = input("IP address + Subnet mask:\t")
            dict_int.setdefault(int, ip_int)
        else:
            break
    net_connect.enable()
    for i in dict_int:
        int_ip = ["interface "+i,
                  "no shut", 
                  "ip address "+ dict_int[i], "exit"]
        print(net_connect.sen_config_set(int_ip))
    print("\n\tDone!!!\n")
    print(net_connect.send_command("show ip int brief"))

#----------------------------------------------------------------------------------------------------------------------------------------#
#Trunking configuration
#----------------------------------------------------------------------------------------------------------------------------------------#

def trunking_config():
    net_connect = ConnectHandler(**info_dev)
    list_trunking = []
    while True:
        end = input("Enter to continue or end to finish.\n")
        if end != 'end':
            int_trunking = input("Interface:\t")
            list_trunking.append(int_trunking)
        else: break
    net_connect.enable()
    for i in list_trunking:
        trunking_config = ["Interface"+ i, 
                           "switchport trunk encapsulation dot1q",
                           "switchport mode trung"]
    print("\n\tDone!!!\n")
    print(net_connect.send_command("show int trunk"))

#----------------------------------------------------------------------------------------------------------------------------------------#
#TVlan configuration
#----------------------------------------------------------------------------------------------------------------------------------------#

def vlan_configuration():
    net_connect = ConnectHandler(**info_dev)
    dict_vlan = {}
    list_int = [] 
    while True:
        end = input("Enter to continue or end to finish.\n")
        if end != "end":
            vlan = input("VLAN\t")
            vlan_name = input("VLAN name:\t")
            print("\nEnter interface apply for VLAN - ex: e0/1, e0/2...\n")
            vlan_int = ("Enter interface:\t")
            dict_vlan.setdefault(vlan, vlan_name)
        else:break
    net_connect.enable()
    for i in dict_vlan:
        vlan_configuration =    ["vlan "+i, 
                                "name "+dict_vlan[i],
                                "exit"]
    print(net_connect.send_config_set(trunking_config))
    print("\n\tDone!!!\n")
    print(net_connect.send_command("show vlan"))            