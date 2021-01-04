from datetime import datetime
import paramiko
from paramiko_expect import SSHClientInteraction
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

class NodeActions():
    def __init__(self):
        super().__init__()
        
    def get_node_list(self):
        node_list = []
        with open("node_list_input.txt") as fileReader:
            node_data = fileReader.read()
            node_list = node_data.splitlines()
            server_list = []
            for elem in node_list:
                server_list.append(elem.split(','))
        return server_list
    
    def get_zombie_number(self, node_details):
        failed_node = []
        
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(node_details[1], username=node_details[2], password=node_details[3])
            interact = SSHClientInteraction(ssh, timeout=60, display=True)
            interact.expect('admin:')
            interact.send('set cli pagination off')
            interact.expect('admin:')
            interact.send('show process load')
            interact.expect('admin:')
            process_output = interact.current_output_clean
            regPattern = re.compile("(\d)\szombie")
            zombie_number = re.search(regPattern, process_output)
            if zombie_number == None:
                print("Some error occured")
            result = zombie_number.groups()[0]
            print("Zombies found: ",result)
            return result 
        except paramiko.AuthenticationException:
                print("\nAuthentication failed for node: ",node_details[1],". Please check the credentials in input file")
                failed_node.append(node_details[1])
        except paramiko.SSHException as SSHException:
                print("\nUnable to establish a SSH connection: ", SSHException)
                print("connection failed for node:",node_details[1])
                failed_node.append(node_details[1])
        except Exception as E:
                print("\nError occured: ", E)
                print("connection failed for node:",node_details[1])
                failed_node.append(node_details[1])

def runner():
    nodeObj = NodeActions()
    all_server = nodeObj.get_node_list()
    zombie_result = {}
    for h in all_server:
        with ThreadPoolExecutor(max_workers=4) as executor:
            func_return = executor.submit(nodeObj.get_zombie_number, h)
            return_value = func_return.result()
            zombie_result[h[0]] = int(return_value)

    return zombie_result

