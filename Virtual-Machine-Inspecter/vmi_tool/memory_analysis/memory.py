import psutil

class MemoryAnalysis:
    def __init__(self):
        pass
    
    def get_memory_info(self):
        """
        Retrieve memory statistics including total, available, used, and free memory.
        :return: Dictionary with memory information.
        """
        mem = psutil.virtual_memory()
        memory_info = {
            "total_memory": f"{mem.total / (1024 ** 3):.2f} GB",
            "available_memory": f"{mem.available / (1024 ** 3):.2f} GB",
            "used_memory": f"{mem.used / (1024 ** 3):.2f} GB",
            "free_memory": f"{mem.free / (1024 ** 3):.2f} GB",
            "memory_percentage": f"{mem.percent} %"
        }
        for key, value in memory_info.items():
                print(f"{key}: {value}")

        return memory_info
    
    def get_swap_memory_info(self):
        """
        Retrieve swap memory statistics including total, used, and free swap memory.
        :return: Dictionary with swap memory information.
        """
        swap = psutil.swap_memory()
        swap_info = {
            "total_swap": f"{swap.total / (1024 ** 3):.2f} GB",
            "used_swap": f"{swap.used / (1024 ** 3):.2f} GB",
            "free_swap": f"{swap.free / (1024 ** 3):.2f} GB",
            "swap_percentage": f"{swap.percent} %"
        }
        for key, value in swap_info.items():
                print(f"{key}: {value}")
        return swap_info
    
    def get_top_memory_consuming_processes(self, count=5):
        """
        Retrieve top memory-consuming processes.
        :param count: Number of top processes to return.
        :return: List of dictionaries with process details.
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                mem_info = proc.info['memory_info']
                processes.append({
                    "pid": proc.info['pid'],
                    "name": proc.info['name'],
                    "memory_used": f"{mem_info.rss / (1024 ** 2):.2f} MB"  # Memory usage in MB
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        # Sort processes by memory usage (descending) and return the top N
        processes = sorted(processes, key=lambda p: float(p['memory_used'].replace(' MB', '')), reverse=True)
        return processes[:count]
    
    def get_top_cpu_consuming_processes(self, count=5):
        """
        Retrieve top CPU-consuming processes.
        :param count: Number of top processes to return.
        :return: List of dictionaries with process details.
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                processes.append({
                    "pid": proc.info['pid'],
                    "name": proc.info['name'],
                    "cpu_usage": f"{proc.info['cpu_percent']} %"  # CPU usage percentage
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        # Sort processes by CPU usage (descending) and return the top N
        processes = sorted(processes, key=lambda p: float(p['cpu_usage'].replace(' %', '')), reverse=True)
        return processes[:count]

