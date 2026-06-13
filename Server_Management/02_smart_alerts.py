import psutil

print("\n--- Smart Server Alerts & Audit ---")

# RAM Check with Alert
ram = psutil.virtual_memory()
if ram.percent >= 80:
    print(f"[WARNING] RAM usage is high: {ram.percent}%")

# Process Audit (Top 3)
print("Top 3 RAM Consuming Processes:")
processes = sorted([p.info for p in psutil.process_iter(['name', 'memory_percent'])], 
                   key=lambda p: p['memory_percent'], reverse=True)
for p in processes[:3]:
    print(f"  - {p['name']}: {p['memory_percent']:.2f}%")

print("----------------------------------\n")