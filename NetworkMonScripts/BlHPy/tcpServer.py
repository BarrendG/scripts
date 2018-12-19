import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

# this is our client handling thread

def handle_client(client_socket):

	# print out what the client sends
	request = client_socket.recv(1024)

	print "[*] Received: %s" % request
	
	# send back a packet
	client_socket.send("ACK!")

while True:
	client, addr = server.accept()

	print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

	# spin up our client thread to handle incoming data
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()

def server_loop():
	global target

	#if no target is defined, we listen on all interfaces
	if not len(target):
		target = "0.0.0.0"

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((target,port))
	server.listen(5)

	while True:
		client_socket, addr = server.accept()

#spin off a thread to handle our new client
		client_thread = threading.Thread(target=client_handler, args(client_socket,))
		client_thread.start()

def run_command(command):
	
#trim the newline
	command = command.rstrip()

#run the command and get the output back
	try:
		output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
	except:
		output = "Failed to execute command. \r\n"
	
# send the output back to the client
	return output
