import os
import subprocess
import datetime

class SnapshotManager:
    def __init__(self, snapshots_dir='snapshots'):
        self.snapshots_dir = snapshots_dir
        if not os.path.exists(self.snapshots_dir):
            os.makedirs(self.snapshots_dir)

    def run_command(self, command):
        """
        Helper method to run system commands and capture output.
        """
        try:
            print(f"Executing command: {' '.join(command)}")  # Debugging line
            result = subprocess.run(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True, 
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e.stderr.strip()}")  # Debugging line
            return f"Error: {e.stderr.strip()}"
        except FileNotFoundError:
            print("Error: VBoxManage not found. Ensure it's installed and in PATH.")
            return "Error: VBoxManage not found."

    def create_snapshot(self, vm_name):
        """
        Create a snapshot of the specified VM.
        """
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        snapshot_name = f"{vm_name}_{timestamp}"

        # Create a snapshot using VBoxManage
        print(f"Creating snapshot '{snapshot_name}' for VM '{vm_name}'...")
        command = ["VBoxManage", "snapshot", vm_name, "take", snapshot_name, "--pause"]
        output = self.run_command(command)

        # Log the snapshot creation details
        snapshot_path = os.path.join(self.snapshots_dir, snapshot_name)
        os.makedirs(snapshot_path, exist_ok=True)
        with open(os.path.join(snapshot_path, 'snapshot.txt'), 'w') as f:
            f.write(f"Snapshot '{snapshot_name}' for VM '{vm_name}' created at {datetime.datetime.now()}.\nDetails:\n{output}")

        return snapshot_name

    def list_snapshots(self, vm_name):
        """
        List all snapshots for the specified VM.
        """
        print(f"Listing snapshots for VM '{vm_name}'...")
        command = ["VBoxManage", "snapshot", vm_name, "list"]
        output = self.run_command(command)

        # Check if there's an error in the command output
        if output.startswith("Error"):
            print(output)
            return []

        # Parse the snapshot list and return as a list of snapshot names
        snapshots = []
        for line in output.splitlines():
            if "Name:" in line:
                snapshots.append(line.split(":")[1].strip())
        return snapshots

    def restore_snapshot(self, snapshot_name, vm_name):
        """
        Restore a snapshot for the specified VM.
        """
        print(f"Restoring snapshot '{snapshot_name}' for VM '{vm_name}'...")
        command = ["VBoxManage", "snapshot", vm_name, "restore", snapshot_name]
        output = self.run_command(command)
        return {
            'message': f"Snapshot '{snapshot_name}' restored for VM '{vm_name}'.",
            'details': output
        }

    def delete_snapshot(self, snapshot_name, vm_name):
        """
        Delete a snapshot for the specified VM.
        """
        print(f"Deleting snapshot '{snapshot_name}' for VM '{vm_name}'...")
        command = ["VBoxManage", "snapshot", vm_name, "delete", snapshot_name]
        output = self.run_command(command)
        return {
            'message': f"Snapshot '{snapshot_name}' deleted for VM '{vm_name}'.",
            'details': output
        }
