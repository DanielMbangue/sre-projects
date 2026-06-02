import subprocess
def check_ping(hostname):
    result = subprocess.run(
        ["ping", "-c", "4",hostname],
        capture_output=True,
        text =True,
        timeout=10
    )
    if result.returncode != 0:
        return (False, None)
    
    for line in result.stdout.split("\n"):
        if "min/avg/max" in line:
            parts = line.split("=")
            numbers = parts[1].strip().replace(" ms", "")
            values = numbers.split("/")
            avg_latency = float(values[1])
            return (True, avg_latency)
    return(True, None)