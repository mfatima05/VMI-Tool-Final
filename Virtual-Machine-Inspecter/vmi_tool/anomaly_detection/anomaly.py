

import numpy as np
import psutil
import threading
import time

class AnomalyDetection:
    def __init__(self):
        self.cpu_usage_history = []
        self.lock = threading.Lock()
        self.stop_event = threading.Event()

    def record_cpu_usage(self):
        """Record the current CPU usage."""
        while not self.stop_event.is_set():
            usage = psutil.cpu_percent(interval=1)
            with self.lock:
                self.cpu_usage_history.append(usage)
    
    def detect_anomalies(self, threshold=2):
        """Detect anomalies in CPU usage."""
        while not self.stop_event.is_set():
            time.sleep(5)  # Adjust frequency of anomaly detection
            with self.lock:
                if len(self.cpu_usage_history) < 2:
                    print('Not enough data to detect anomalies.')
                    continue

                # Convert history to a numpy array for easy computation
                data = np.array(self.cpu_usage_history)
                mean = np.mean(data)
                std_dev = np.std(data)

                # Detect anomalies as data points that are more than `threshold` standard deviations away from the mean
                anomalies = np.where(np.abs(data - mean) > threshold * std_dev)[0]
                
                if len(anomalies) > 0:
                    print('Anomalies detected:')
                    for idx in anomalies:
                        print(f'Anomaly at index {idx} with value {data[idx]:.2f}%')

    def start_detection(self):
        """Start the anomaly detection and data collection."""
        self.recording_thread = threading.Thread(target=self.record_cpu_usage)
        self.detection_thread = threading.Thread(target=self.detect_anomalies)
        
        self.recording_thread.start()
        self.detection_thread.start()

    def stop_detection(self):
        """Stop the anomaly detection and data collection."""
        self.stop_event.set()
        self.recording_thread.join()
        self.detection_thread.join()

    def get_cpu_usage_history(self):
        """Get the history of recorded CPU usage."""
        with self.lock:
            return self.cpu_usage_history

