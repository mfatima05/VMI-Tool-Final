import psutil
import winrm

class VMICore:
    def __init__(self, vm_name, remote_host=None, username=None, password=None):
        """
        Initialize the VMICore class.
        :param vm_name: Name of the virtual machine or target machine.
        :param remote_host: (Optional) IP or hostname for the remote machine.
        :param username: (Optional) Username for remote machine authentication.
        :param password: (Optional) Password for remote machine authentication.
        """
        self.vm_name = vm_name
        self.remote_host = remote_host
        self.username = username
        self.password = password
        self.session = None
    
    def connect(self):
        """
        Connect to the local or remote machine.
        """
        if self.remote_host:
                # Establish WinRM session for remote VM monitoring
                self.session = winrm.Session(self.remote_host, auth=(self.username, self.password))
        self.connected = True
            
    def disconnect(self):
        """sel
        Disconnect from the remote or local machine.
        """
        if self.session:
                self.session.close()
        self.connected = False
            
    def get_vm_info(self):
        """
        Retrieve system information for the local or remote VM.
        :return: Dictionary with VM info.
        """
        if self.remote_host:
            command = "systeminfo"
            result = self.session.run_cmd(command)
            return result.std_out.decode()
        else:
            # Get system information using psutil for local VM
            vm_info = {
                "name": self.vm_name,
                "cpu_count": psutil.cpu_count(),
                "memory": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
                "used_memory": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
                "uptime": self.get_uptime(),
                "processes": len(psutil.pids())
            }
            for key, value in vm_info.items():
                print(f"{key}: {value}")
            return vm_info
    
    def get_uptime(self):
        """
        Get system uptime.
        """
        boot_time = psutil.boot_time()
        uptime_seconds = psutil.time.time() - boot_time
        uptime_hours = uptime_seconds / 3600
        return f"{uptime_hours:.2f} hours"
    
    def start_vm(self):
        """
        Placeholder for starting a VM.
        """
        print(f"Start VM functionality is not supported for local machines using psutil.")

    def stop_vm(self):
        """
        Placeholder for stopping a VM.
        """
        print(f"Stop VM functionality is not supported for local machines using psutil.")
    
    def reboot_vm(self):
        """
        Reboot the remote VM via WinRM.
        """
        if self.remote_host:
            command = "shutdown /r /t 0"
            result = self.session.run_cmd(command)
            if result.status_code == 0:
                print(f"Remote VM {self.remote_host} is rebooting.")
            else:
                print(f"Failed to reboot the remote VM. Error: {result.std_err.decode()}")
        else:
            print("Reboot functionality is not supported for local machines.")
