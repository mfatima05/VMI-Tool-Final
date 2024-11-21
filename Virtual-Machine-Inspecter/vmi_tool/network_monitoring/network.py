import psutil
import socket

class NetworkMonitoring:
    def __init__(self):
        pass
    
    def get_network_interfaces(self):
        """
        Retrieve details of all network interfaces including IP addresses and stats.
        :return: Dictionary with network interface information.
        """
        interfaces = psutil.net_if_addrs()
        interface_stats = psutil.net_if_stats()
        
        interface_info = {}
        for interface_name, addresses in interfaces.items():
            interface_info[interface_name] = {
                'is_up': interface_stats[interface_name].isup,
                'speed': interface_stats[interface_name].speed,
                'mtu': interface_stats[interface_name].mtu,
                'addresses': []
            }
            for address in addresses:
                interface_info[interface_name]['addresses'].append({
                    'family': str(address.family),
                    'address': address.address,
                    'netmask': address.netmask,
                    'broadcast': address.broadcast
                })
        return interface_info

    def get_active_connections(self):
        connections = psutil.net_connections(kind='inet')
        connection_list = []
        for conn in connections:
            connection_list.append({
                'type': 'TCP' if conn.type == socket.SOCK_STREAM else 'UDP',
                'local_address': f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else None,
                'remote_address': f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else None,
                'status': conn.status
            })
        return connection_list

    def get_network_io_stats(self):
        """
        Retrieve network I/O statistics (bytes sent/received).
        :return: Dictionary with I/O statistics for each interface.
        """
        net_io = psutil.net_io_counters(pernic=True)
        io_stats = {}
        for interface, stats in net_io.items():
            io_stats[interface] = {
                'bytes_sent': f"{stats.bytes_sent / (1024 ** 2):.2f} MB",
                'bytes_recv': f"{stats.bytes_recv / (1024 ** 2):.2f} MB",
                'packets_sent': stats.packets_sent,
                'packets_recv': stats.packets_recv
            }
        return io_stats

# Example usage
if __name__ == "__main__":
    nm = NetworkMonitoring()
    nm.get_network_interfaces()
    nm.get_active_connections()
    nm.get_network_io_stats()
