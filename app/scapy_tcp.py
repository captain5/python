import sys  
import struct  
from scapy.all import *  
  
data = struct.pack('ssssssss','w','a','n','g','p','e','n','g')  
pkt = IP(src='10.0.3.83', dst='10.0.3.88')/TCP(sport=12345,dport=5555)/data  
send(pkt, inter=1, count=5) 
