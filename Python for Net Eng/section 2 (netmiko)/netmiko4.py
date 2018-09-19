from netmiko import ConnectHandler

# 5 variables for 5 remote devices
# One Python Dictionary per remote device
ios_l2_sw2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.82',
	'username': 'cisco',
	'password': 'cisco'
}

ios_l2_sw3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.83',
	'username': 'cisco',
	'password': 'cisco'
}

ios_l2_sw4 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.84',
	'username': 'cisco',
	'password': 'cisco'
}

ios_l2_sw5 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.85',
	'username': 'cisco',
	'password': 'cisco'
}

ios_l2_sw6 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.86',
	'username': 'cisco',
	'password': 'cisco'
}

# Read a file and split its lines
# The 'print' command is optional, but provides visibility
with open('access_switch_configs.txt') as f:
	lines = f.read().splitlines()
print (lines)

# A list of the 3 access devices that we want to connect
access_devices = [ios_l2_sw4, ios_l2_sw5, ios_l2_sw6]

# A 'for' loop which connects to the remote devices
# I sents the configuration read from the file
# The 'print' will show us what is applied
for devices in access_devices:
	net_connect = ConnectHandler(**devices)
	output = net_connect.send_config_set(lines)
	print (output)
	
	
# Read a file and split its lines
# The 'print' command is optional, but provides visibility
with open('all_switch_configs.txt') as f:
	lines = f.read().splitlines()
print (lines)

# A list of all the devices that we want to connect
all_devices = [ios_l2_sw2, ios_l2_sw3, ios_l2_sw4, ios_l2_sw5, ios_l2_sw6]

# A 'for' loop which connects to the remote devices
# I sents the configuration read from the file
# The 'print' will show us what is applied
for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	output = net_connect.send_config_set(lines)
	print (output)