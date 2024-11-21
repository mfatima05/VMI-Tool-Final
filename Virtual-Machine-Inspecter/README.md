<h1>VMI Tool - Virtual Machine Introspection for Security Monitoring</h1>
This project provides a comprehensive Virtual Machine Introspection (VMI) tool, built using Python, to monitor, analyze, and ensure the security of virtual machines. The tool supports monitoring various aspects of VM health and performance, such as CPU, memory, processes, file system, network, and detecting potential anomalies and malware. The tool can also take snapshots and alert on security breaches.

<h2>Features</h2>

•	VM Information: Get core VM information, including CPU, memory, uptime, and processes.<br>

•	Memory Analysis: Monitor memory usage over time.<br>

•	Network Monitoring: Analyze active connections and network statistics.<br>

•	Process Monitoring: Monitor and analyze running processes in the VM.<br>

•	File System Monitoring: Check disk usage and file statistics.<br>

•	CPU Monitoring: Track CPU usage across multiple cores.<br>

•	Anomaly Detection: Detect unusual patterns in resource usage (CPU, memory).<br>

•	Snapshot Management: Take snapshots of the VM and restore them if needed.<br>

•	Logging: Log all activity for auditing purposes.<br>

•	Malware Analysis: Scan files and directories for malware using ClamAV.<br>

•	GUI and CLI Interface: Use either a command-line interface or a graphical user interface for interaction.<br>


<h2>Project Structure</h2>

```bash
vmi_tool/
│
├── anomaly_detection/
│   └── anomaly.py
├── cpu_monitoring/
│   └── cpu.py
├── file_system_monitoring/
│   └── filesystem.py
├── logging/
│   └── logger.py
├── malware_analysis/
│   └── malware_analysis.py
├── memory_analysis/
│   └── memory.py
├── network_monitoring/
│   └── network.py
├── process_monitoring/
│   └── process.py
├── snapshot_manager/
│   └── snapshot.py
├── vmi_core/
│   └── core.py
├── gui_interface/
│   └── gui.py
├── cli_interface/
│   └── cli.py
├── utils/
│   └── utils.py
├── main.py
└── README.md
```

<h2>Prerequisites</h2>

- Python 3.8 or higher 
-	psutil
-	pyclamd (for malware analysis)
-	tkinter (for GUI)
-	pywinrm (for Windows Remote Management)

<h2>Installation</h2>

Install Python Dependencies
```bash
pip install psutil pyclamd pywinrm tkinter
```
Run the tool with various actions using the following commands:
```bash
python main.py --vm <vm_name> --action <action> [--options]
```
 <h3>Available Actions</h3>
 
- Show VM Info:
  ```bash
  python main.py --vm <vm_name> --action info
  ```
- Memory Analysis:
  ```bash
  python main.py --vm <vm_name> --action memory
  ```
- Network Monitoring:
  ```bash
  python main.py --vm <vm_name> --action network
  ```
- Process Monitoring:
  ```bash
  python main.py --vm <vm_name> --action processes
  ```
- File System Monitoring:
  ```bash
  python main.py --vm <vm_name> --action filesystem
  ```
- CPU Monitoring:
  ```bash
  python main.py --vm <vm_name> --action cpu
  ```
- Anomaly Detection:
  ```bash
  python main.py --vm <vm_name> --action anomaly
  ```
- Snapshot Management:
  ```bash
  python main.py --vm <vm_name> --action snapshot --snapshot <snapshot_name> --operation [create|restore|delete]
  ```
- Malware Analysis:
  ```bash
  python main.py --vm <vm_name> --action malware-analysis --directory <directory_path>
  ```
- Command Line Interface (CLI):
  
  Run the tool with various actions using the following commands: 
  ```bash
  python main.py --vm <vm_name> --action <action> [--options]
  ```
- Graphical User Interface (GUI):
  
  To launch the tool in GUI mode, use:
  ```bash
  python main.py --gui
  ```

<h3>Running the Tool</h3>
python3 main.py -h

<h2>Contributing</h2>

If you wish to contribute, feel free to fork this repository, create a new branch, and submit a pull request.

<h2>Futute Scope</h2>
We can incorporate malware analysis capabilities into this project to detect, analyze, and respond to malicious software more effectively. This could include adding automated tools for malware scanning, behavioral analysis, and threat intelligence integration to enhance overall security.

<h2>License</h2>

This project is licensed under the MIT . See the <a href="https://github.com/Khyati-33/Virtual-Machine-Inspecter/blob/main/LICENSE">LICENSE</a> file for more details.

<h2>Contact</h2>
For any questions or issues, please contact:

**Khyati Sharma** - \[ https://github.com/Khyati-33 ] <br>
**Maseera Fatima** - \[https://github.com/mfatima05]

