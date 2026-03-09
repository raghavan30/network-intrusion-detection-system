# Network Intrusion Detection System (IDS)

## Overview
This project implements a basic Network Intrusion Detection System (IDS) using Python and Scapy.  
The IDS monitors network traffic in real time and detects abnormal port access patterns that may indicate a port scanning attack.

The system captures packets, analyzes TCP traffic, and generates alerts when suspicious activity is detected.

## Lab Environment

Attacker Machine:
Kali Linux  
IP Address: 192.168.56.107

IDS Machine:
Ubuntu  
IP Address: 192.168.56.108

## Tools and Technologies

Python  
Scapy  
Wireshark  
Nmap  
Linux

## Features

- Real-time packet capture
- Detection of abnormal port access
- Alert generation for suspicious IP addresses
- Logging of detected attacks
- Packet validation using Wireshark

## How the IDS Works

1. Captures TCP packets using Scapy
2. Extracts source IP address and destination port
3. Tracks the number of ports accessed by each IP
4. Detects abnormal behavior when the number of accessed ports exceeds a threshold
5. Generates an alert and logs the suspicious IP address

## Attack Simulation

A port scanning attack was simulated using Nmap from the Kali Linux machine targeting the Ubuntu IDS machine.

Example command used:

nmap -p 1-1000 192.168.56.108

The IDS detected the scanning behavior and generated alerts for the attacking IP address.

## Results

The IDS successfully identified abnormal port access from the attacking machine and recorded the event in the alert log.

## Screenshots

Screenshots of the following are included in the repository:

- Nmap port scan from Kali Linux
- IDS alert detection in terminal
- Packet capture verification using Wireshark

## Project Architecture

Kali Linux (Attacker)
192.168.56.107
        │
        │ Nmap Port Scan
        ▼
Ubuntu IDS
192.168.56.108
        │
        │ Packet Inspection (Scapy)
        ▼
Alert Generated
alerts.log
