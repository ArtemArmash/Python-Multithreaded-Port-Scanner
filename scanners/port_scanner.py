from targets.target import Target
from scapy.all import IP, TCP, sr1, send
import threading
import socket
class PortScanner:
    
    def __init__(self, target_object, ports_to_scan):
        if target_object.ip_address is None:
            raise ValueError("IP-адрес не определён. Невозможно просканировать.")
        
        self.target_object = target_object
        self.port_to_scan = ports_to_scan
        
        self.open_ports = []
        self.lock = threading.Lock()
        
    def _scan_port(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            result = sock.connect_ex((self.target_object.ip_address, port))
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    
    def scan(self):
        print('Начало сканирования\n')
        threads = []
        
        for port in self.port_to_scan:
            thread = threading.Thread(target=self._scan_port, args=(port,))
            threads.append(thread)
            thread.start()
            
        for thread in threads:
            thread.join()
        
        self.open_ports.sort()
        
        return {
            "target": self.target_object.hostname,
            "ip_address": self.target_object.ip_address,
            "open_ports": self.open_ports
        }
        
                
        