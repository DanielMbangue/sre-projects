import subprocess

def run_traceroute(hostname, max_hops=15):
    try:
        result = subprocess.run(
            ["traceroute", "-m", str(max_hops), "-w", "2", "-q", "1", hostname],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.stdout
    except subprocess.TimeoutExpired:
        return None