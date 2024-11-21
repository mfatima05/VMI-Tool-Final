

class Help:
    def show_help(self):
        help_text = """
        VMI Tool Packages:
        1. vmi_core: Core functionalities related to VM interaction.
        2. memory_analysis: Analyzes memory dumps for potential threats.
        3. network_monitoring: Monitors and analyzes network traffic.
        4. process_monitoring: Tracks and analyzes running processes.
        5. file_system_monitoring: Monitors file system changes for malicious activity.
        6. cpu_monitoring: Monitors CPU usage and detects anomalies.
        7. anomaly_detection: Implements algorithms for detecting anomalies.
        8. snapshot_manager: Manages VM snapshots and rollbacks.
        9. logging: Logs events and generates reports.
        10. hypervisor_monitoring: Monitors interactions with the hypervisor.
        11. kernel_integrity: Performs kernel integrity checks.
        12. alerts: Sends alerts when security issues are detected.
        13. cli_interface: Provides a command-line interface for the tool.
        14. gui_dashboard: Offers a graphical user interface for monitoring.
        15. utils: Utility functions for the tool.
        """
        print(help_text)

