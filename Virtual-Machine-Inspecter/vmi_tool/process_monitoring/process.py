import psutil

class ProcessMonitoring:
    def __init__(self):
        pass
    
    def get_all_processes(self):
        """
        Retrieve a list of all running processes with basic details.
        :return: List of dictionaries with process details.
        """
        process_list = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                process_list.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu_percent': proc.info['cpu_percent'],
                    'memory_used': f"{proc.info['memory_info'].rss / (1024 ** 2):.2f} MB"  # Memory usage in MB
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        # Print processes with formatted output
        print("\nAll Running Processes:\n" + "-" * 50)
        for proc in process_list:
            print(f"PID: {proc['pid']:<10} Name: {proc['name']:<20} "
                  f"CPU: {proc['cpu_percent']:<5} Memory: {proc['memory_used']:<10}")
        return process_list
    
    def get_process_info(self, pid):
        """
        Retrieve detailed information about a specific process by PID.
        :param pid: Process ID.
        :return: Dictionary with detailed process information.
        """
        try:
            proc = psutil.Process(pid)
            process_info = {
                'PID': proc.pid,
                'Name': proc.name(),
                'Status': proc.status(),
                'CPU Usage': f"{proc.cpu_percent(interval=1):.2f}%",
                'Memory Used': f"{proc.memory_info().rss / (1024 ** 2):.2f} MB",  # Memory usage in MB
                'Created At': proc.create_time(),
                'Executable Path': proc.exe()
            }
            
            # Print detailed process info
            print("\nProcess Details:\n" + "-" * 50)
            for key, value in process_info.items():
                print(f"{key:<15}: {value}")
            return process_info
        
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            print("Error: Process not found or access denied")
            return None
    
    def get_top_cpu_memory_processes(self, count=5):
        """
        Retrieve top processes by CPU and memory usage.
        :param count: Number of top processes to return.
        :return: List of dictionaries with process details.
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu_percent': proc.info['cpu_percent'],
                    'memory_used': f"{proc.info['memory_info'].rss / (1024 ** 2):.2f} MB"  # Memory usage in MB
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        # Sort processes by CPU and memory usage (descending) and return the top N
        processes_by_cpu = sorted(processes, key=lambda p: p['cpu_percent'], reverse=True)[:count]
        processes_by_memory = sorted(processes, key=lambda p: float(p['memory_used'].replace(' MB', '')), reverse=True)[:count]
        
        # Print top CPU and memory consuming processes
        print("\nTop CPU-Consuming Processes:\n" + "-" * 50)
        for proc in processes_by_cpu:
            print(f"PID: {proc['pid']:<10} Name: {proc['name']:<20} CPU: {proc['cpu_percent']:<5} Memory: {proc['memory_used']:<10}")
        
        print("\nTop Memory-Consuming Processes:\n" + "-" * 50)
        for proc in processes_by_memory:
            print(f"PID: {proc['pid']:<10} Name: {proc['name']:<20} CPU: {proc['cpu_percent']:<5} Memory: {proc['memory_used']:<10}")
        
        return {
            'top_cpu': processes_by_cpu,
            'top_memory': processes_by_memory
        }
