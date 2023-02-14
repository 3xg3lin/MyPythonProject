import subprocess
import optparse
import re

def opt_func():                           # getting user input value
    object = optparse.OptionParser()
    object.add_option('-i','--interface',dest='interface',help='which interface to change')
    object.add_option('-m','--mac',dest='mac_address',help='new mac adress')
    return object.parse_args()

def subprocess_func(object_interface,object_mac_address):                    #changing mac address
    subprocess.run(['ip','link','set',object_interface,'down'])
    subprocess.run(['ip','link','set',object_interface,'address',object_mac_address])
    subprocess.run(['ip','link','set',object_interface,'up'])

def check_mac_address(interface):                                     #control for mac_address
    iplink= subprocess.check_output(['ip','link','show',interface])
    new_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w',str(iplink))
    if new_mac:
        return new_mac.group(0)
    else:
        print('Something went wrong!')

(user_input,arguments) = opt_func()
subprocess_func(user_input.interface,user_input.mac_address)
finally_mac = check_mac_address(str(user_input.interface))

if finally_mac == user_input.mac_address:
    print('success!')
else:
    print('Something went wrong !?')

