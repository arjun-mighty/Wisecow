import psutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in %
MEMORY_THRESHOLD = 80  # in %
DISK_THRESHOLD = 80  # in %

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    running_processes = len(psutil.pids())
    
    alert_message = []
    
    if cpu_usage > CPU_THRESHOLD:
        alert_message.append(f'High CPU usage detected: {cpu_usage}%')
    if memory_usage > MEMORY_THRESHOLD:
        alert_message.append(f'High Memory usage detected: {memory_usage}%')
    if disk_usage > DISK_THRESHOLD:
        alert_message.append(f'High Disk usage detected: {disk_usage}%')
    
    if alert_message:
        message = '\n'.join(alert_message)
        print("ALERT!", message)
        logging.warning(message)
    else:
        logging.info(f'System is healthy: CPU {cpu_usage}%, Memory {memory_usage}%, Disk {disk_usage}%, Running Processes {running_processes}')
    
if __name__ == "__main__":
    check_system_health()

