from dns_check import check_dns 
from http_check import check_http 
from ping_check import check_ping
from port_check import check_common_ports
from traceroute_check import run_traceroute
import sys

def run_diagnostics(hostname):
    print(f" === Network Diagnostic for {hostname} ===\n")
    print("[1] DNS Resolution...")
    result = check_dns(hostname)
    if result is None:
        print(f"Failure! - Couldn't retrieve: {hostname}")
        return 
    print(f"Success - IP retrived:  {result}")

    print("[2] Ping Test...")
    success,latency = check_ping(hostname)
    if not success:
        print("Failure! - host unreachable (may block ICMP)")
    else:
        print(f"Success! - average latency {latency}")
    
    print("[3] Port Check...")
    ports = check_common_ports(hostname)
    for port, is_open in ports.items():
        status = "OPEN" if is_open else "closed"
        print(f"  Port {port}: {status}") 

   
    print("[4] HTTP Status Check...")
    url = None
    if ports[443]:
        url = f"https://{hostname}"
    elif ports[80]:
        url = f"http://{hostname}"
    else:
        print("    SKIPPED — no web ports open")
    
    if url is not None:
        success, status, elapsed = check_http(url)
        if success:
            print(f"    OK — status {status} in {elapsed:.1f} ms")
        elif status is not None:
            print(f"    Server returned status {status}")
        else:
            print(f"    FAILED — could not connect")  
    
    print("[5] Traceroute...")
    result = run_traceroute(hostname)
    if result is None:
        print("FAILED — traceroute could not complete")
    else:
        print(result)
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python network_diag.py <hostname>")
        sys.exit(1)
    run_diagnostics(sys.argv[1])


