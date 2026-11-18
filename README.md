# Basic Network Sniffer

**CodeAlpha Cyber Security Internship – Task 1**

## Project Overview

Basic Network Sniffer is a Python-based network monitoring tool developed using Scapy. It captures and analyzes network packets and displays useful information about network communication.

## Features

- Live network packet capturing
- Source and destination IP identification
- TCP, UDP and ICMP protocol detection
- Packet filtering by protocol
- Source and destination port identification
- Packet length analysis
- Timestamp display
- Payload preview when available
- Packet capture statistics
- Automatic packet information logging

## Technologies Used

- Python
- Scapy
- Npcap
- Visual Studio Code

## Installation

1. Install Python.
2. Install Npcap on Windows.
3. Clone this repository.
4. Create a virtual environment.

```bash
python -m venv venv
```

5. Activate the environment.

```powershell
venv\Scripts\activate
```

6. Install dependencies.

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python sniffer.py
```

Choose a packet filtering option:

1. ALL
2. TCP
3. UDP
4. ICMP

Press `CTRL + C` to stop capturing packets and view statistics.

## Project Structure

```text
CodeAlpha_BasicNetworkSniffer/
│
├── sniffer.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

## Ethical Considerations

This project is developed for educational purposes and authorized network monitoring only. Do not capture or inspect traffic on networks without permission.

## Internship

Developed as part of the CodeAlpha Cyber Security Internship.