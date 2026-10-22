from sentinel.parser import parse_failed_login

def test_failed_login_invalid_user():
	line = "Oct 11 14:10:01 server sshd[1201]: Failed password for invalid user admin from 192.168.1.50 port 50122 ssh2"
	
	result = parse_failed_login(line)

	assert result["event"] == "failed_login"
	assert result["username"] == "admin"
	assert result["invalid_user"] is True
	assert result["ip"] == "192.168.1.50"
	assert result["port"] == 50122


def test_failed_login_root():
	line = "Oct 11 14:10:05 server sshd[1202]: Failed password for root from 192.168.1.50 port 50123 ssh2"

	result = parse_failed_login(line)

	assert result["event"] == "failed_login"
	assert result["username"] == "root"
	assert result["invalid_user"] is False
	assert result["ip"] == "192.168.1.50"
	assert result["port"] == 50123


def test_accepted_login_returns_none():
	line = "Oct 11 14:10:14 server sshd[1204]: Accepted password for fili from 192.168.1.20 port 54444 ssh2"
	
	result = parse_failed_login(line)

	assert result is None
