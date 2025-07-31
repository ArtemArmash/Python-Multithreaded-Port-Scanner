import socket

class Target:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip_address = self._resolve()
    def _resolve(self):
        try:
            socket.inet_aton(self.hostname)
            return self.hostname
        except socket.error:
            try:
                return socket.gethostbyname(self.hostname)
            except socket.gaierror:
                print(f'Не удалось определить IP-адрес')
                return None
            
        
    
    
            
            