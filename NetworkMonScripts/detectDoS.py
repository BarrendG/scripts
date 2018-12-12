import dpkt
import socket
THRESH = 10000
def findAttack(pcap):
	pktCount = {}
	for (ts, buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			tcp = ip.data
			dport = tcp.dport
			if dport == 80:
				stream = src + ':' + dst
				if pktCount.has_key(stream):
					pktCount[stream] = pktCount[stream] + 1
				else:
					pktCount[stream] = 1
		except:
			pass
	for stream in pktCount:
		pktsSent = pktCount[stream]
		if pktsSent > THRESS:
			src = stream.split(':')[0]
			dst = stream.split(':')[1]
			print '[+] '+src+' attacked ' +dst+ ' with ' + str(pktsSent) + ' pkts.'
