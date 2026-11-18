from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

LOG_FILE = "captured_packets.txt"

# Packet statistics
packet_stats = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "OTHER": 0
}

# Select protocol
print("\n===== BASIC NETWORK SNIFFER =====")
print("1. ALL")
print("2. TCP")
print("3. UDP")
print("4. ICMP")

choice = input("\nSelect protocol (1-4): ")

protocol_options = {
    "1": "ALL",
    "2": "TCP",
    "3": "UDP",
    "4": "ICMP"
}

selected_protocol = protocol_options.get(choice)

if selected_protocol is None:
    print("Invalid selection!")
    exit()


# Filter packets
def packet_filter(packet):

    if IP not in packet:
        return False

    if selected_protocol == "ALL":
        return True

    if selected_protocol == "TCP":
        return TCP in packet

    if selected_protocol == "UDP":
        return UDP in packet

    if selected_protocol == "ICMP":
        return ICMP in packet

    return False


# Analyze packets
def analyze_packet(packet):

    ip = packet[IP]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if TCP in packet:
        protocol = "TCP"
        packet_stats["TCP"] += 1

    elif UDP in packet:
        protocol = "UDP"
        packet_stats["UDP"] += 1

    elif ICMP in packet:
        protocol = "ICMP"
        packet_stats["ICMP"] += 1

    else:
        protocol = "OTHER"
        packet_stats["OTHER"] += 1

    details = [
        "\n========== PACKET DETAILS ==========",
        f"Time           : {timestamp}",
        f"Source IP      : {ip.src}",
        f"Destination IP : {ip.dst}",
        f"Protocol       : {protocol}",
        f"Packet Length  : {len(packet)} bytes"
    ]

    if TCP in packet:
        details.append(f"Source Port    : {packet[TCP].sport}")
        details.append(f"Destination Port: {packet[TCP].dport}")

    elif UDP in packet:
        details.append(f"Source Port    : {packet[UDP].sport}")
        details.append(f"Destination Port: {packet[UDP].dport}")

    # Analyze packet payload
    if Raw in packet:
        payload = packet[Raw].load
        details.append(f"Payload Preview: {repr(payload[:50])}")
    else:
        details.append("Payload: No raw payload available")


    details.append("====================================")

    output = "\n".join(details)

    # Display packet details
    print(output)

    # Save packet details
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(output + "\n")


# Display statistics
def show_statistics():

    print("\n========== CAPTURE STATISTICS ==========")

    total = sum(packet_stats.values())

    print("Total Packets :", total)
    print("TCP Packets   :", packet_stats["TCP"])
    print("UDP Packets   :", packet_stats["UDP"])
    print("ICMP Packets  :", packet_stats["ICMP"])
    print("Other Packets :", packet_stats["OTHER"])

    print("========================================")


# Start capture
print("\nNetwork Sniffer Started!")
print("Selected Protocol:", selected_protocol)
print("Capturing packets... Press CTRL+C to stop.")

try:

    sniff(
        prn=analyze_packet,
        store=False,
        lfilter=packet_filter
    )

except KeyboardInterrupt:

    print("\nNetwork Sniffer Stopped!")

    show_statistics()

    print("\nPacket logs saved in:", LOG_FILE)
