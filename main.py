from targets.target import Target
from scanners.port_scanner import PortScanner
from utils.report_generator import ReportGenerator
import sys
url = "google.com"
ports = [80,443,20,23,4134,21,22,2]
target_obj = Target(url)

if target_obj.ip_address is None:
    sys.exit(1)

scanner_obj = PortScanner(target_obj, ports)
result_to_scan = scanner_obj.scan()

report_generator_obj = ReportGenerator()
report_generator_obj.generate_console(result_to_scan)
report_generator_obj.generate_json(result_to_scan, "result.json")
