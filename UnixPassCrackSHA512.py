import crypt
def testPass(cryptPass):
	ctype= "6"
	salt="Ug1ZA3.A"
	insalt = '${}${}$'.format(ctype,salt)
	dictFile = open ('dictionary.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,insalt)
		if (cryptWord == cryptPass):
			print "[+] Found Password: "+word+"\n"
			return
	print "[-] Password Not Found.\n"
	return
def main():
	passFile = open('passwords.txt')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1]
			print "[*] Cracking Password For: "+user
			testPass(cryptPass)
if __name__=="__main__":
	main()

