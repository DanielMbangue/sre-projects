import socket
def check_port(host, port, timeout=2):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    result = sock.connect_ex((host,port))
    sock.close()
    if result == 0:
        return True
    return False

def check_common_ports(host):
    ports_to_check = [22, 80, 443, 8080, 3306, 5432]
    results = {}
    for i in ports_to_check:
        results[i] = check_port(host,i)
    return results

if __name__ == "__main__":
    print(check_common_ports("google.com"))