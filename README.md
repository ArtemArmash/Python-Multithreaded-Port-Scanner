# Python Multithreaded Port Scanner

This project is a powerful and efficient command-line port scanning tool built with Python. It is designed to quickly identify open ports on a target host by leveraging multithreading for parallel scanning. The tool is architected with a clean, modular structure, separating responsibilities for target resolution, scanning, and reporting.

## About The Project

This project serves as an excellent practical example of network programming and concurrent execution in Python. It's a great portfolio piece for anyone interested in cybersecurity, network administration, or advanced Python development. The code is well-organized, easy to understand, and extensible.

### Key Concepts and Features

*   **Modular Architecture**: The project is logically divided into three main components:
    *   **`targets`**: A module for defining and resolving the target host (domain name or IP address).
    *   **`scanners`**: The core scanning engine, which performs the port scan.
    *   **`utils`**: Utilities for generating scan reports in different formats.
*   **Multithreading for Performance**: The scanner uses the `threading` module to scan multiple ports simultaneously, dramatically reducing the time it takes to complete a scan compared to a sequential approach.
*   **Network Socket Programming**: Utilizes the `socket` library to perform TCP connect scans (`connect_ex`), a reliable method for checking if a port is open.
*   **Robust Target Resolution**: The `Target` class can resolve both domain names (e.g., `google.com`) and direct IP addresses.
*   **Multiple Report Formats**: The `ReportGenerator` class can output the scan results in two formats:
    *   A clean, human-readable summary printed to the console.
    *   A structured JSON file (`result.json`) for easy parsing and integration with other tools.
*   **Clean, Object-Oriented Code**: The entire application is built using classes, encapsulating data and behavior for better maintainability and readability.

## Project Structure

The project directory is organized as follows, which promotes a clean separation of concerns:

```
.
├── main.py                 # Main entry point of the application
├── result.json             # Example JSON output file
├── scanners/
│   ├── __init__.py
│   └── port_scanner.py     # Contains the PortScanner class
├── targets/
│   ├── __init__.py
│   └── target.py           # Contains the Target class
└── utils/
    ├── __init__.py
    └── report_generator.py # Contains the ReportGenerator class
```

## How to Set Up and Run

To run this project, you need Python 3 installed on your system.

### 1. Installation

There are no external libraries needed for the core functionality, but the provided code snippet in `port_scanner.py` imports `scapy`. While `scapy` is not used in the `_scan_port` method, if you intend to expand the project with other scan types (like SYN scans), you will need it.

To install `scapy` (optional, for future development):
```sh
pip install scapy
```

### 2. How to Run

1.  **Clone or Download the Repository**:
    ```sh
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    ```
2.  **Navigate to the Project Directory**:
    ```sh
    cd YOUR_REPOSITORY_NAME
    ```
3.  **Run the Main Script**:
    Execute the `main.py` file from your terminal:
    ```sh
    python main.py
    ```

### 4. Customizing a Scan

You can easily change the target and the list of ports to scan by editing the `main.py` file:

```python
# In main.py
url = "example.com"  # Change the target here
ports = # Change the list of ports to scan here
```

## Example Output

When you run the script, you will see a progress message in the console, followed by a report.

### Console Output:

```
Начало сканирования

----- Отчет по сканированию -----
Цель: google.com
IP-адрес: 142.250.203.142
Открытые порты: 80, 443
-------------------------------
```

### JSON File (`result.json`):
A file named `result.json` will be created in the root directory with the following content:

```json
{
    "target": "google.com",
    "ip_address": "142.250.203.142",
    "open_ports": [
        80,
        443
    ]
}
```
```
