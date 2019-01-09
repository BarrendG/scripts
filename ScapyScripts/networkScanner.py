import sys
from scapy.all import sr1,IP,ICMP

def netscan():
	a=str(sys.argv)
	p=sr1(IP(src="127.0.0.1",dst=a)/ICMP())
