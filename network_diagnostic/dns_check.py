import socket
def check_dns(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return None 

print(check_dns("google.com"))
print(check_dns("notarealdomain123xyz.com"))
