

import psutil
import time


class CPUMonitoring:
    def __init__(self):
        self.dos_attack_threshold = 50  # CPU usage threshold for DoS detection (in %)
        self.dos_attack_duration = 2   # Duration in seconds to detect sustained high usage
        self.dos_attack_flag = False   # Flag to track if DoS attack is detected

    def get_cpu_usage(self):
        """Get the current CPU usage percentage."""
        return {'cpu_usage': f"{psutil.cpu_percent(interval=1):.2f}%"}

    def get_cpu_stats(self):
        """Get CPU frequency and times stats."""
        cpu_freq = psutil.cpu_freq()
        cpu_times = psutil.cpu_times()
        
        return {
            'cpu_frequency': f"{cpu_freq.current:.2f} MHz" if cpu_freq else 'N/A',
            'cpu_times': {
                'user': f"{cpu_times.user:.2f} seconds",
                'system': f"{cpu_times.system:.2f} seconds",
                'idle': f"{cpu_times.idle:.2f} seconds"
            }
        }

    def get_cpu_core_usage(self):
        """Get CPU usage per core."""
        return {
            f'core_{i}': f"{percent:.2f}%"
            for i, percent in enumerate(psutil.cpu_percent(percpu=True, interval=1))
        }

    def get_cpu_temperature(self):
        """Get CPU temperature."""
        try:
            temperatures = psutil.sensors_temperatures()
            if 'coretemp' in temperatures:
                return {
                    'cpu_temperature': f"{temperatures['coretemp'][0].current:.2f} °C"
                }
            else:
                return {'error': 'Temperature sensors not available or not supported on this system.'}
        except Exception as e:
            return {'error': str(e)} 

    def detect_dos_attack(self):
        """Detect potential DoS attack based on sustained high CPU usage."""
        sustained_high_usage_start = None

        while True:
            current_cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU Usage: {current_cpu_usage:.2f}%")

            if current_cpu_usage > self.dos_attack_threshold:
                if not sustained_high_usage_start:
                    sustained_high_usage_start = time.time()
                elif time.time() - sustained_high_usage_start >= self.dos_attack_duration:
                    if not self.dos_attack_flag:
                        print("Potential DoS attack detected! High CPU usage sustained.")
                        self.dos_attack_flag = True
            else:
                sustained_high_usage_start = None
                self.dos_attack_flag = False

if __name__ == "__main__":
    monitor = CPUMonitoring()

    # Start monitoring for DoS attacks
    print("Monitoring system for potential DoS attacks...")
    monitor.detect_dos_attack()

