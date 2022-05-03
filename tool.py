import config
options = """   \n\nAdmin: Ngo Truong Hai\n
1 - Xem thông tin thiết bị.
2 - Cấu hình Interface (R).         
3 - Cấu hình Trunking (SW)
4 - Cấu hình VLAN (SW)
5 - Cấu hình access VLAN (SW)
6 - Cấu hình routing
7 - Cấu hình Access list
...
e - Exit
"""

while True:
    print(options)
    option = int(input("choose mode: \t"))
    def choice(option):
        match option:
            case 0:
                print("Exit") 
            case 1:
                config.info_device() 
            case 2:
                config.interface_config()
            case 3:
                config.trunking_config()
            case 4:
                config.vlan_config()
            case 5:
                config.access_int_vlan_config()
            case 6:
                config.routing_config()
            #wildcard case
            case _:
                print("Please Enter a Valid Number")
                return False
    choice(option)