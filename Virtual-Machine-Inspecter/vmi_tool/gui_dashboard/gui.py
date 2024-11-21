

import tkinter as tk
from tkinter import messagebox
import psutil
import time

class GUIInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Machine Introspection Tool's GUI")
        self.setup_ui()

    def setup_ui(self):
        # Add widgets here
        label = tk.Label(self.root, text="Welcome to our VMI Tool")
        label.pack(pady=10)

        info_button = tk.Button(self.root, text="Show Info", command=self.show_info)
        info_button.pack(pady=5)

    def get_system_info(self):
        """Retrieve core system information."""
        try:
            vm_info = {
                "CPU Count": psutil.cpu_count(),
                "Memory Total": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
                "Memory Used": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
                "Uptime": self.get_uptime(),
                "Processes": len(psutil.pids())
            }
            return vm_info
        except Exception as e:
            return {'error': str(e)}

    def get_uptime(self):
        """Calculate system uptime."""
        try:
            boot_time = psutil.boot_time()
            uptime_seconds = time.time() - boot_time
            hours, remainder = divmod(uptime_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
        except Exception as e:
            return {'error': str(e)}

    def show_info(self):
        """Show core system information in a messagebox."""
        info = self.get_system_info()
        if 'error' in info:
            messagebox.showerror("Error", info['error'])
        else:
            info_str = "\n".join([f"{key}: {value}" for key, value in info.items()])
            messagebox.showinfo("System Information", info_str)

def main():
    root = tk.Tk()
    app = GUIInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()

