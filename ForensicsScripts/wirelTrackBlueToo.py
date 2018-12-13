import time
from bluetooth import *
alreadyFound = []
def findDevs():
	foundDevs = discover_devices(lookup_names=True)
	for device in devList:
		if addr not in alreadyFound:
			print "[+] Found Bluetooth Device " + str(name)
			print "[+] MAC address: "+str(device)
			already.Found.append(addr)
	while True:
		findDevs()
		time.sleep(5)
