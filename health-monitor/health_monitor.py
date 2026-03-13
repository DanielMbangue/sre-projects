import psutil
from datetime import datetime

def get_system_stats():
  cpu_percent = psutil.cpu_percent()
  virtual_memory = psutil.virtual_memory().percent
  disk_usage = psutil.disk_usage('/').percent

  return(cpu_percent,virtual_memory,disk_usage)

def check_thresholds(cpu_percent,virtual_memory,disk_usage):
    if cpu_percent > 80:
       print(f"Warning!! passed threshold, CPU percentage: {cpu_percent}")
       log_warning(f"CPU percentage: {cpu_percent}%")
    if virtual_memory > 80:
       print(f"Warning!! passed threshold, Virtual Memory percentage: {virtual_memory}")
       log_warning(f"Virtual Memory percentage: {virtual_memory}%")
    if disk_usage > 90:
        print(f"Warning!! passed threshold, Disk_Usage: {disk_usage}")
        log_warning(f"Disk Usage percentage: {disk_usage}%")

def log_warning(message):
    with open('health_log.txt', 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} -- WARNING: {message}\n")
      
   


def main():
   try:
    cpu,virt,disk = get_system_stats()
    print(f"CPU Usage: {cpu}%")
    print(f"Virtual Memory Usage: {virt}%")
    print(f"Disk Usage: {disk}%")

    check_thresholds(cpu,virt,disk)
   except FileNotFoundError:
    print("File not found!")
   except KeyboardInterrupt:
    print("Monitor Stopped")
main()