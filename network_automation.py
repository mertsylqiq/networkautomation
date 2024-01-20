from netmiko import ConnectHandler

def configure_dhcp(device_ip, username, password, dhcp_pool_name, subnet, start_ip, end_ip, gateway):
    device = {
        'device_type': 'cisco_ios',
        'ip': device_ip,
        'username': username,
        'password': password,
        'secret': password,  
    }

    try:
        with ConnectHandler(**device) as net_connect:
            net_connect.enable()

            dhcp_config_commands = [
                f'ip dhcp pool {dhcp_pool_name}',
                f'network {subnet} /24',
                f'default-router {gateway}',
                f'address {start_ip} {end_ip}',
            ]

            output = net_connect.send_config_set(dhcp_config_commands)

            print("DHCP configuration successful. Output:\n", output)

    except Exception as e:
        print(f"An error occurred during DHCP configuration: {str(e)}")

def configure_ospf(device_ip, username, password, ospf_process_id, router_id, network_list):
    device = {
        'device_type': 'cisco_ios',
        'ip': device_ip,
        'username': username,
        'password': password,
        'secret': password,  
    }

    try:
        with ConnectHandler(**device) as net_connect:
            net_connect.enable()

            ospf_config_commands = [
                f'router ospf {ospf_process_id}',
                f'router-id {router_id}',
            ]

            ospf_config_commands.extend([f'network {network} area 0' for network in network_list])

            output = net_connect.send_config_set(ospf_config_commands)

            print("OSPF configuration successful. Output:\n", output)

    except Exception as e:
        print(f"An error occurred during OSPF configuration: {str(e)}")

if __name__ == "__main__":
    device_ip = 'YOUR_DEVICE_IP'
    username = 'YOUR_USERNAME'
    password = 'YOUR_PASSWORD'

    dhcp_pool_name = 'my_dhcp_pool'
    subnet = '192.168.1.0'
    start_ip = '192.168.1.10'
    end_ip = '192.168.1.50'
    gateway = '192.168.1.1'

    ospf_process_id = '1'
    router_id = '1.1.1.1'
    network_list = ['192.168.1.0', '192.168.2.0']  

    configure_dhcp(device_ip, username, password, dhcp_pool_name, subnet, start_ip, end_ip, gateway)
    configure_ospf(device_ip, username, password, ospf_process_id, router_id, network_list)
