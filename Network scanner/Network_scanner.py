import scapy.all
import optparse

def user_ip_range():
    instance = optparse.OptionParser()
    instance.add_option("-r","--range",dest="range",help="enter your ip range for scaning")
    user_input,arguments = instance.parse_args()
    return user_input.range
    
    if not user_input.range:
        print('please enter a ip address')


def arp_func(ip):
    arp_request = scapy.all.ARP(pdst=ip)
    #scapy.all.ls(scapy.all.ARP())
    broadcast = scapy.all.Ether(dst='ff:ff:ff:ff:ff:ff')
    #scapy.all.ls(scapy.all.Ether())
    combined_packet = broadcast/arp_request
    answered_list,unanswered_list = scapy.all.srp(combined_packet,timeout=1)
    answered_list.summary()

arp_func(user_ip_range())