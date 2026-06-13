import psutil
import time

print("\n--- Smart Process Killer ---")

# The name of the software we want to find and stop
target_process = "notepad.exe" 

found = False

# Search through all running processes
for proc in psutil.process_iter(['pid', 'name']):
    try:
        # Check if the process name matches our target
        if proc.info['name'] and proc.info['name'].lower() == target_process.lower():
            print(f"[ALERT] Target process found: {proc.info['name']} (PID: {proc.info['pid']})")
            print("Action: Terminating process in 3 seconds...")
            
            # Wait for 3 seconds so you can see it happening
            time.sleep(3) 
            
            # Kill the process
            proc.kill()
            print(f"[SUCCESS] Process {proc.info['name']} (PID: {proc.info['pid']}) has been successfully terminated!")
            
            found = True
            break # Stop looking after we kill it
            
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

if not found:
    print(f"[INFO] Process '{target_process}' is not currently running. System is safe.")
    
print("----------------------------\n")