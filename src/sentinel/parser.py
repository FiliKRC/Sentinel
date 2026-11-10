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

def parse_file(path):
	events = []

	with open(path, "r") as file:
		for line in file:
			log = parse_failed_login(line)

			if log is not None:
				events.append(log)

	return events

def main():
	op = parse_file("samples/auth.log")
	print(op)

if __name__ == "__main__":
	main()
