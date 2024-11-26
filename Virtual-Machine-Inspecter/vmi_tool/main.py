from vmi_core.core import VMICore


from memory_analysis.memory import MemoryAnalysis
from network_monitoring.network import NetworkMonitoring
from malware_analysis.malware import MalwareDetection
from process_monitoring.process import ProcessMonitoring
from file_system_monitoring.filesystem import FileSystemMonitoring
from cpu_monitoring.cpu import CPUMonitoring
from anomaly_detection.anomaly import AnomalyDetection
from snapshot_manager.snapshot import SnapshotManager
from gui_dashboard.gui import GUIInterface
from help.help import Help
import argparse
import time
import tkinter as tk
import pyclamd
import scapy 
import json 


def print_intro():
    print("""
                 VIRTUAL MACHINE INTROSPECTION TOOL
                           Developed by
                             ~Maseera
 
      Happy Testing :)
    
    """)

def main():
   # Print intro text
  print_intro()
  # Parse command-line arguments
  parser = argparse.ArgumentParser(
        description="Virtual Machine Introspection (VMI) Tool - Developed by Khyati and Maseera."
  )
  parser = argparse.ArgumentParser(description="Virtual Machine Introspection (VMI) Tool")
  parser.add_argument('--vm', type=str, required=True, help='Name of the virtual machine.')
  parser.add_argument('--action', type=str, required=True, choices=['help','info', 'reboot', 'memory', 'network', 'process', 'filesystem', 'cpu', 'anomaly', 'snapshot','alerts', 'gui', 'malware-analysis'], help='Action to perform on the virtual machine.')
  parser.add_argument('--remote', type=str, help='IP or hostname for the remote VM.')
  parser.add_argument('--snapshot', type=str, help='Snapshot name for restore action. (Only required if action is "snapshot" and sub-action is restore)')
  parser.add_argument('--user', type=str, help='Username for the remote VM.')
  parser.add_argument('--password', type=str, help='Password for the remote VM.')
  parser.add_argument('--pid', type=int, help='Process ID for detailed process information.')
  parser.add_argument('--path', type=str, default='.', help='Path for file system monitoring (default is current directory).')
  parser.add_argument('--visualize', type=str, choices=['usage', 'core', 'temperature'], help='Type of visualization for CPU monitoring.')
  args = parser.parse_args()
    
  vmi = VMICore(args.vm, remote_host=args.remote, username=args.user, password=args.password)

  try:
    vmi.connect()
    if args.action == 'info':
        info = vmi.get_vm_info()
        print("\nVM Information:")
        print(json.dumps(info, indent=4))

    elif args.action == 'reboot':
        vmi.reboot_vm()

    elif args.action == 'memory':
        # Perform memory analysis
        mem_analysis = MemoryAnalysis()
        
        swap_info = mem_analysis.get_swap_memory_info()
        print("\nSwap Info:", swap_info)
        # Retrieve top memory-consuming processes
        top_memory_processes = mem_analysis.get_top_memory_consuming_processes()
        print("\nTop Memory-Consuming Processes:")
        for process in top_memory_processes:
         print(f"PID: {process['pid']}, Name: {process['name']}, Memory Used: {process['memory_used']}")
         # Retrieve top CPU-consuming processes
         top_cpu_processes = mem_analysis.get_top_cpu_consuming_processes()
        print("\nTop CPU-Consuming Processes:") 
        for process in top_cpu_processes:
         print(f"PID: {process['pid']}, Name: {process['name']}, CPU Usage: {process['cpu_usage']}")



    elif args.action == 'network':
      # Perform network monitoring
      net_monitor = NetworkMonitoring()
      # Get network interfaces and print them in a pretty format
      interfaces = net_monitor.get_network_interfaces()
      print("\nNetwork Interfaces:")
      print(json.dumps(interfaces, indent=4))  # Pretty print the network interfaces
      # Get active connections and print them in a pretty format
      active_connections = net_monitor.get_active_connections()
      print("\nActive Connections:")
      print(json.dumps(active_connections, indent=4))  # Pretty print the active connections
      # Get network I/O stats and print them in a pretty format
      io_stats = net_monitor.get_network_io_stats()
      print("\nNetwork I/O Stats:")
      print(json.dumps(io_stats, indent=4))  # Pretty print the network I/O stats


    elif args.action == 'process':
      # Perform process monitoring
      proc_monitor = ProcessMonitoring()
      if args.pid:
        # Fetch and display detailed process information
        process_info = proc_monitor.get_process_info(args.pid)
        if process_info:
            print("\nProcess Information Retrieved Successfully.")
        else:
            print("\nFailed to retrieve process information.")
      else:
        # Fetch and display all processes
        all_processes = proc_monitor.get_all_processes()
        # Fetch and display top CPU and memory consuming processes
        top_processes = proc_monitor.get_top_cpu_memory_processes()


    elif args.action == 'filesystem':
     # Perform file system monitoring
     fs_monitor = FileSystemMonitoring()
     if args.path:
        # Fetch and display disk usage
        print("\nFetching Disk Usage Information...\n")
        disk_usage = fs_monitor.get_disk_usage(args.path)
     else:
        print("\nNo path specified. Using default (current directory).\n")
        args.path = '.'  # Default path
     # Fetch and display files and directories
     print("\nListing Files and Directories...\n")
     files_and_dirs = fs_monitor.list_files_and_directories(args.path)
     # Fetch and display file system statistics
     print("\nFetching File System Statistics...\n")
     fs_stats = fs_monitor.get_file_system_stats()


    elif args.action == 'cpu':
        cpu_monitor = CPUMonitoring()
        cpu_usage = cpu_monitor.get_cpu_usage()
        print("CPU Usage:", cpu_usage)
        cpu_stats = cpu_monitor.get_cpu_stats()
        print("\nCPU Stats:", cpu_stats)
        core_usage = cpu_monitor.get_cpu_core_usage()
        print("\nCPU Core Usage:", core_usage)
        cpu_temperature = cpu_monitor.get_cpu_temperature()
        print("CPU Temperature:",cpu_temperature)
        print("\nStarting DoS attack detection based on CPU usage...")
        try:
            cpu_monitor.detect_dos_attack()
        except KeyboardInterrupt:
            print("\nStopping CPU monitoring")
            print("\nNo DoS attack detected. CPU usage is normal")


    elif args.action == 'anomaly':
        anomaly_detector = AnomalyDetection()
        anomaly_detector.start_detection()
        # Run detection for a specified amount of time
        try:
            time.sleep(40)  # Collect data and detect anomalies for 60 seconds
        finally:
            anomaly_detector.stop_detection()
            print("\nFinal CPU Usage History:", anomaly_detector.get_cpu_usage_history())


    elif args.action == 'snapshot':
     snapshot_manager = SnapshotManager()
     if args.snapshot and args.restore:
        # Restore an existing snapshot
        restore_result = snapshot_manager.restore_snapshot(args.snapshot, args.vm)
        if 'message' in restore_result:
            print(f"Success: {restore_result['message']}")
        if 'details' in restore_result:
            print(f"Details: {restore_result['details']}")
        else:
            print("Failed to restore snapshot.")
     elif args.snapshot and args.delete:
        # Delete an existing snapshot
        delete_result = snapshot_manager.delete_snapshot(args.snapshot, args.vm)
        if 'message' in delete_result:
            print(f"Success: {delete_result['message']}")
        if 'details' in delete_result:
            print(f"Details: {delete_result['details']}")
        else:
            print("Failed to delete snapshot.")
     elif args.action == 'snapshot' and args.snapshot is None:
         # List all snapshots for the specified VM
        snapshots = snapshot_manager.list_snapshots(args.vm)
        print(f"Snapshots for VM '{args.vm}':")
        for snapshot in snapshots:
            print(f"- {snapshot}")
     else:
        # Create a new snapshot
        snapshot_name = snapshot_manager.create_snapshot(args.vm)
        print(f"Snapshot created successfully: {snapshot_name}")


    elif args.action == 'malware-analysis':
     # Perform malware analysis
     malware_analyzer = MalwareDetection(
        known_malware_hashes={"knownhash1", "knownhash2"},
        suspicious_extensions={'.exe', '.bat', '.py'}
     )
     print("\nPerforming Malware Analysis...")
     # Simulate scanning a user-specified directory
     directory = args.path if args.path else "C:/path/to/suspicious/directory"
     print(f"\nScanning directory: {directory}")
     suspicious_files = malware_analyzer.scan_directory_for_malware(directory)
     if suspicious_files:
        print("\nSuspicious Files Found:")
        for file in suspicious_files:
            print(f"- {file}")
     else:
        print("\nNo suspicious files found in the directory.")
     # Check running processes
     running_processes = malware_analyzer.get_running_processes()
     print("\nRunning Processes:")
     if running_processes:
        print(json.dumps(running_processes, indent=4))
     else:
        print("No running processes retrieved.")
     # Check file integrity
     # Assuming the known_good_hashes are provided for integrity checks
     known_good_hashes = {
        "C:/path/to/suspicious/directory/file1.exe": "expectedhash1",
        "C:/path/to/suspicious/directory/file2.bat": "expectedhash2"
     }
     file_integrity = malware_analyzer.check_file_integrity(directory, known_good_hashes)
     print("\nFile Integrity Status:")
     print(json.dumps(file_integrity, indent=4))

    elif args.action == 'gui':
        root = tk.Tk()
        app = GUIInterface(root)
        root.mainloop()


    elif args.action == 'help':
        help_text = Help()
        help_text.show_help()
       
  except Exception as e:
    print(f"An error occured: {e}")

  finally:
        vmi.disconnect()

if __name__ == "__main__":
    main()



