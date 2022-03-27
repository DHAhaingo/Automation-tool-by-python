# from netmiko import ConnectHandler

# #Router R1
# SW = {
#     'device_type':'cisco_ios',
#     'host': '172.16.0.107',
#     'username': 'hai',
#     'password': 'dtu@123456',
#     'secret':'dtu@123456',
# }

# net_connect= ConnectHandler(**R1)
# net_connect.enable()
# for n in range (1,10):
#     addLoopbacks = ['int loop' +str(n), 'ip add 10.0.'+str(n)+'.1 255.255.255.0']
#     out1 = net_connect.send_config_set(addLoopbacks)
#     print(out1)
# out2 = net_connect.sen_command('show ip int br')
# print(out2)

# #
