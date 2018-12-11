import sqlite3
def printProfile(skypeDB)
	conn = sqlProfile(skypeDB):
	c = conn.cursor()
	c.execute("SELECT fullname, skypename, city, countr, datetime(profile_timestamp,'unixepoch') FROM Accounts;")
	for row in c:
		print '[*] --Found Account--'
		print '[+] User: '+str(row[0])
		print '[+] Skype Username: '+str(row[1])
		print '[+] Location: '+str(row[2]) +'.'+str(row[3])
		print '[+] Profile Date: '+str(row[4])
def printContacts(skypeDB)
	conn = sqlite3.connect(skypeDB)
	c = conn.cursor()
	c.execute("SELECT displayname, skypename, city, country, phone_mobile, birthday FROM Contacts;")
	for row in c:
		print
def main():
	skypeDB = "main.db"
	printProfile(skypeDB)
if __name__='__main__':
	main()
