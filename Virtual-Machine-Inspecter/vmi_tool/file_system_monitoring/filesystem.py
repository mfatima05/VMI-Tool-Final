from vmi_core.core import VMICore
connector = VMICore("Ubuntu")  # Replace with actual VM name
connector.connect()
import os
import psutil

class FileSystemMonitoring:
    def __init__(self):
        pass
    
    def get_disk_usage(self, path='C:\\'):
        """
        Retrieve disk usage statistics for the specified path.
        :param path: Path to get disk usage information for (default is C:\).
        :return: Dictionary with disk usage statistics.
        """
        # Ensure the path is absolute and normalized
        path = os.path.abspath(path)
        
        # Check if the path exists
        if not os.path.exists(path):
            print(f"\nError: Path {path} does not exist.\n")
            return None
        
        try:
            # Get disk usage statistics
            usage = psutil.disk_usage(path)
            stats = {
                'Total Space': f"{usage.total / (1024 ** 3):.2f} GB",
                'Used Space': f"{usage.used / (1024 ** 3):.2f} GB",
                'Free Space': f"{usage.free / (1024 ** 3):.2f} GB",
                'Usage Percent': f"{usage.percent:.2f}%"
            }
            
            print(f"\nDisk Usage for Path: {path}\n" + "-" * 50)
            for key, value in stats.items():
                print(f"{key:<15}: {value}")
            return stats
        except Exception as e:
            print(f"\nError retrieving disk usage: {str(e)}\n")
            return None
    
    def list_files_and_directories(self, path='.'):
        """
        List all files and directories in the specified path.
        :param path: Directory path to list files and directories from (default is current directory).
        :return: List of dictionaries with file and directory names.
        """
        # Ensure the path is absolute
        path = os.path.abspath(path)
        
        # Check if the path exists
        if not os.path.exists(path):
            print(f"\nError: Path {path} does not exist.\n")
            return None
        
        print(f"\nFiles and Directories in Path: {path}\n" + "-" * 50)
        file_list = []
        for entry in os.scandir(path):
            file_info = {
                'Name': entry.name,
                'Type': 'Directory' if entry.is_dir() else 'File',
                'Size': f"{entry.stat().st_size / (1024 ** 2):.2f} MB" if entry.is_file() else "N/A"
            }
            file_list.append(file_info)
            print(f"Name: {file_info['Name']:<30} Type: {file_info['Type']:<10} Size: {file_info['Size']}")
        return file_list
    
    def get_file_system_stats(self):
        """
        Retrieve file system statistics including total, used, and free space.
        :return: Dictionary with file system statistics.
        """
        partitions = psutil.disk_partitions()
        stats = {}
        print("\nFile System Statistics:\n" + "-" * 50)
        for partition in partitions:
            partition_stats = self.get_disk_usage(partition.mountpoint)
            stats[partition.device] = partition_stats
            print(f"\nDevice: {partition.device}")
            if partition_stats:
                for key, value in partition_stats.items():
                    print(f"{key:<15}: {value}")
        return stats
    
connector.disconnect()