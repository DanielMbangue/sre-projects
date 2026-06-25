import psutil
from datetime import datetime

def get_system_stats():
    cpu_percent = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return (cpu_percent, virtual_memory, disk_usage)


# PURE DECISION FUNCTION - easy to test, no side effects
# Given the stats, return a list of warning messages (empty list = all healthy)
def get_threshold_warnings(cpu_percent, virtual_memory, disk_usage):
    warnings = []
    if cpu_percent > 80:
        warnings.append(f"CPU percentage: {cpu_percent}%")
    if virtual_memory > 80:
        warnings.append(f"Virtual Memory percentage: {virtual_memory}%")
    if disk_usage > 90:
        warnings.append(f"Disk Usage percentage: {disk_usage}%")
    return warnings


def log_warning(message, filename='health_log.txt'):
    with open(filename, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} -- WARNING: {message}\n")


def check_thresholds(cpu_percent, virtual_memory, disk_usage):
    # now this just takes the decisions and acts on them
    warnings = get_threshold_warnings(cpu_percent, virtual_memory, disk_usage)
    for message in warnings:
        print(f"Warning!! passed threshold, {message}")
        log_warning(message)


def main():
    try:
        cpu, virt, disk = get_system_stats()
        print(f"CPU Usage: {cpu}%")
        print(f"Virtual Memory Usage: {virt}%")
        print(f"Disk Usage: {disk}%")
        check_thresholds(cpu, virt, disk)
    except KeyboardInterrupt:
        print("Monitor Stopped")


if __name__ == "__main__":
    main()