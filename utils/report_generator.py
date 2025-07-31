import json
from datetime import datetime
class ReportGenerator:
    
    def generate_json(self, data, filename):
        data_scan = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
    
    def generate_console(self, data):
        print("----- Отчет по сканированию -----")
        print(f"Цель: {data.get('target', 'Неизвестно')}")
        print(f"IP-адрес: {data.get('ip_address', 'Неизвестно')}")
        open_ports = data.get('open_ports', [])
        if open_ports:
            print("Открытые порты:", ", ".join(str(port) for port in sorted(open_ports)))
        else:
            print("Открытые порты: не обнаружены")
        print("-------------------------------")
        