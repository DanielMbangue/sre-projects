# Network Diagnostic Tool

A command-line network diagnostic tool that runs a layered set of checks against any hostname to identify where in the network stack a problem lives. Built as a Python learning project exploring real SRE diagnostic workflows.

## What It Does

Runs five checks in dependency order — each layer is meaningful only if the previous one worked:

1. **DNS Resolution** — resolves the hostname to an IP address. Hard stop if this fails.
2. **Ping Test** — sends ICMP echo requests to verify the host is reachable, reports average latency.
3. **Port Check** — tests common TCP ports (22, 80, 443, 8080, 3306, 5432) to see which services are listening.
4. **HTTP Status Check** — if a web port is open, makes a GET request and reports the status code and response time.
5. **Traceroute** — maps the full network path to the destination, showing each hop and its latency.

## Requirements

- Python 3.8 or higher
- `requests` library (`pip3 install requests`)
- `ping` and `traceroute` commands available on the system (standard on macOS and Linux)

## Installation

```bash
git clone https://github.com/DanielMbangue/sre-projects.git
cd sre-projects/network_diagnostic
pip3 install requests
```

## Usage

```bash
python3 network_diag.py <hostname>
```

### Example

```bash
python3 network_diag.py google.com
```

### Sample Output

=== Network Diagnostic for google.com ===
[1] DNS Resolution...
Success - IP retrieved: 142.251.163.102
[2] Ping Test...
Success! - average latency 13.7 ms
[3] Port Check...
Port 22: closed
Port 80: OPEN
Port 443: OPEN
Port 8080: closed
Port 3306: closed
Port 5432: closed
[4] HTTP Status Check...
OK — status 200 in 91.2 ms
[5] Traceroute...
1  cr1000a (192.168.1.1)  8.857 ms
2  lo0-100.washdc-vfttp-326.verizon-gni.net (108.31.159.1)  12.677 ms

## Architecture

The tool is split into one file per check, with `network_diag.py` acting as the orchestrator. Each check module is independently testable and reusable.

| File | Responsibility |
|------|----------------|
| `dns_check.py` | DNS resolution via `socket.gethostbyname` |
| `ping_check.py` | ICMP ping via `subprocess`, parses latency from output |
| `port_check.py` | TCP port checks via `socket.connect_ex` |
| `http_check.py` | HTTP GET requests via `requests`, captures status and timing |
| `traceroute_check.py` | Traceroute via `subprocess` |
| `network_diag.py` | Orchestrates checks in the correct dependency order |

## Author

Daniel Mbangue
