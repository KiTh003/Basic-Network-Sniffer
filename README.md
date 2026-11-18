# Basic Network Sniffer

A Python-based network monitoring tool that captures and analyzes network packets in real time using the Scapy library.

## Overview

Basic Network Sniffer is a simple network analysis application designed to monitor network traffic and inspect packet information. It helps users understand how data travels across a network by displaying important packet details and identifying different network protocols.

## Features

- **Live Packet Capturing:** Capture network packets in real time.
- **IP Address Analysis:** Display source and destination IP addresses.
- **Protocol Detection:** Identify TCP, UDP, and ICMP protocols.
- **Protocol Filtering:** Filter captured packets based on selected protocols.
- **Port Information:** Display source and destination port numbers when available.
- **Packet Details:** Display packet length and payload previews when available.
- **Timestamp:** Display the time each packet is captured.
- **Packet Statistics:** View packet counts and protocol statistics.
- **Logging:** Save captured packet information to a text file.

## Technologies Used

- Python
- Scapy
- Npcap
- Visual Studio Code

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Npcap

Install Npcap on Windows if it is not already installed.

Official website: https://npcap.com/

## How to Run

Run the application using:

```bash
python sniffer.py
```

Select your preferred packet filtering option from the displayed menu.

**Available Options:**

1. All Packets
2. TCP Packets
3. UDP Packets
4. ICMP Packets

The application displays captured packet information and provides statistics when packet capturing is stopped.

## Project Structure

```text
Basic-Network-Sniffer/
│
├── sniffer.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── captured_packets.txt
```

*Note: The captured packet log file is generated when the application runs.*

## Learning Outcomes

Through this project, I explored:

- Network traffic monitoring.
- Packet capturing and analysis.
- TCP, UDP, and ICMP protocols.
- IP addressing and port information.
- Python-based network programming.
- Basic network security concepts.

## Ethical Considerations

This tool is intended for educational purposes and authorized network monitoring only. Always obtain permission before capturing or analyzing network traffic. Do not inspect or collect private information belonging to others.

## Author

**Kithmi Githara**

GitHub: https://github.com/KiTh003

---

*Developed as an independent Python networking and cybersecurity learning project.*