# PyRecon Framework

A simple, modular, and extensible network reconnaissance framework written in Python. This project is the result of my education in systems programming and cybersecurity fundamentals.

## Features

- **Object-Oriented Design:** The code is divided into logical classes (`Target`, `PortScanner`, `ReportGenerator`), making it easy to understand and extend.
- **Multi-threaded scanning:** The port scanner uses multi-threading to quickly scan a range of ports.
- **Error handling:** Built-in checks for target and IP address correctness.
- **Flexible reports:** Scan results can be output to console or saved to a structured JSON file.

## Project Structure

PyRecon/
├── main.py # Main entry point to the application
├── scanners/
│ └── port_scanner.py # Class for port scanning
├── targets/
│ └── target.py # Class for managing targets (DNS resolving)
└── utils/
└── report_generator.py # Class for generating reports

## How to use

1. Make sure you have Python 3 and the Scapy library installed:
```bash
pip install scapy
```
2. Edit `main.py` to specify the desired target (`hostname`) and ports to scan.
3. Run the script from the project root:
```bash
sudo python3 main.py
```
*(`sudo` privileges are required to send SYN packets with Scapy).*

4. The results will be printed to the console and also saved to the `.json` file.

## Future plans

- Adding new scanner types (e.g. directory search, UDP scanning).
- Reading targets from the configuration file.
- Improving error handling and output.

---
*The project was developed as part of intensive self-study. Author: Artem*