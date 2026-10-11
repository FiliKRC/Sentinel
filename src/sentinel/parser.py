def parse_failed_login(line):

	prefix, message = line.split(": ", 1)

	if "Failed password" not in message:
		return None
	
	parts = message.split()

	if "invalid user" in message:
		username = parts[5]
		invalid_user = True
		ip = parts[7]
		port = int(parts[9])

	else:
		username = parts[3]
		invalid_user = False
		ip = parts[5]
		port = int(parts[7])
		

	evento = {
		  "event": "failed_login",
		  "username": username,
		  "invalid_user": invalid_user,
		  "ip": ip,
		  "port": port
		 }
	
	return evento

def main():
	line = "Oct 11 14:10:05 server sshd[1202]: Failed password for root from 192.168.1.50 port 50123 ssh2"
	evento = parse_failed_login(line)
	print(evento)

if __name__ == "__main__":
	main()
