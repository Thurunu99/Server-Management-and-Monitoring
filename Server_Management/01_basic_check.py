import psutil

print("\n--- Basic Server Health Check ---")

# CPU Usage
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

# RAM Usage
ram = psutil.virtual_memory()
print(f"Total RAM: {ram.total / (1024 ** 3):.2f} GB")
print(f"Used RAM: {ram.used / (1024 ** 3):.2f} GB ({ram.percent}%)")

# Storage Usage
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")

print("----------------------------------\n")