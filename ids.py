from scapy.all import sniff
from scapy.layers.inet import IP, TCP

ip_ports = {}
THRESHOLD = 10

def log_alert(ip):
    with open("alerts.log", "a") as f:
        f.write(f"Port scan detected from {ip}\n")

def packet_callback(packet):

    if packet.haslayer(IP) and packet.haslayer(TCP):

        src_ip = packet[IP].src
        dst_port = packet[TCP].dport

        print(f"Traffic: {src_ip} -> Port {dst_port}")

        if src_ip not in ip_ports:
            ip_ports[src_ip] = set()

        ip_ports[src_ip].add(dst_port)

        if len(ip_ports[src_ip]) > THRESHOLD:
            print(f"[ALERT] Port scanning detected from {src_ip}")
            log_alert(src_ip)

sniff(iface="enp0s8", filter="tcp", prn=packet_callback, store=0)

