import scapy.all
import optparse

def user_input():
    instance = optparse.OptionParser()
    instance.add_option("-i","--interface",dest="interface",help="which interface you want to sniff")
    optinons = instance.parse_args()[0]
    if not optinons.interface:
        print("please enter interface")
    return optinons.interface

def packet_sniff(interface):
    scapy.all.sniff(iface=interface,prn=lambda packet_list:packet_list.sprintf("{IP:%IP.src% --> %IP.dst%\n}{Raw:%Raw.load%\n}"))

packet_sniff(user_input())