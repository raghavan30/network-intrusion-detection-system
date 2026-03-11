# 📡 Network Intrusion Detection System (IDS) – Python + Scapy

## 📖 Overview

This project demonstrates a **basic Network Intrusion Detection System (IDS)** built using Python and Scapy.

The IDS monitors network traffic in real time, analyzes packet headers, and detects suspicious activities such as **port scanning attacks**. When abnormal behavior is detected, the system generates alerts and logs the attacker's IP address.

This project simulates how **Security Operations Centers (SOC)** monitor and detect network threats.

---

## 🎯 Objective

Build a simple IDS that:

* Captures network packets in real time
* Inspects TCP traffic
* Detects abnormal port access
* Identifies possible port scanning attacks
* Generates alerts and logs suspicious IPs
* Validates traffic using Wireshark
* Documents the project in GitHub

---

## 🛠️ Technologies Used

| Tool         | Purpose                         |
| ------------ | ------------------------------- |
| Ubuntu Linux | IDS monitoring machine          |
| Kali Linux   | Attack simulation machine       |
| Python 3     | IDS script development          |
| Scapy        | Packet sniffing & analysis      |
| Wireshark    | Network traffic verification    |
| Nmap         | Port scanning simulation        |
| Git & GitHub | Version control & documentation |

---

## 🏗️ Architecture

```
Kali Linux (Attacker)
192.168.56.107
        │
        │  Port Scan (Nmap)
        ▼
Ubuntu IDS Machine
192.168.56.108
        │
        │  Packet Capture (Scapy)
        ▼
Detection Engine
        │
        ▼
Alert Generated
alerts.log
```

---

## ⚙️ Implementation Steps

### 1️⃣ Install Required Tools

```
sudo apt update
sudo apt install python3 python3-pip wireshark git
pip3 install scapy
```

---

### 2️⃣ Capture Packets in Real Time

The IDS uses Scapy to capture network packets:

```
sniff(filter="tcp", prn=packet_callback, store=0)
```

The system monitors TCP traffic and extracts:

* Source IP
* Destination port

---

### 3️⃣ Detect Abnormal Port Access

The IDS tracks the number of ports accessed by each IP address.

If the number of accessed ports exceeds the threshold, the system flags a **possible port scanning attack**.

Example logic:

```
If IP accesses more than 10 ports
→ Trigger alert
```

---

### 4️⃣ Generate Alerts

When suspicious behavior is detected:

```
[ALERT] Port scanning detected from 192.168.56.107
```

The alert is also logged to:

```
alerts.log
```

---

### 5️⃣ Simulate Attack Using Nmap

On the Kali Linux machine:

```
nmap -p 1-1000 192.168.56.108
```

This simulates a **port scanning attack** against the IDS machine.

---

### 6️⃣ Validate Traffic Using Wireshark

Wireshark was used to verify captured packets.

Filter used:

```
tcp
```

Observed packets from attacker machine:

```
192.168.56.107 → 192.168.56.108 TCP SYN
```


---

### Run IDS Script

```
sudo python3 ids.py
```

The system will start monitoring network traffic in real time.

---

### Simulate Attack

From the attacker machine:

```
nmap -p 1-1000 <target-ip>
```

Example:

```
nmap -p 1-1000 192.168.56.108
```

---

## 🚨 Features

* Real-time packet monitoring
* TCP traffic analysis
* Port scan detection
* Alert generation
* Attack logging
* Wireshark verification
* Open-source security implementation

---

## 📌 Learning Outcomes

This project demonstrates practical skills in:

* Network packet analysis
* Intrusion detection systems
* Python security scripting
* Network attack simulation
* Blue team monitoring techniques
* Security project documentation

---

## 📸 Screenshots

### IDS Monitoring Traffic

<img width="940" height="85" alt="image" src="https://github.com/user-attachments/assets/e59e1ef1-ac2b-44f2-9f36-08f49a235ef1" />
<img width="940" height="602" alt="image" src="https://github.com/user-attachments/assets/65bca0de-6d14-48b6-9096-b031b62d4567" />



---

### Nmap Port Scan Attack

<img width="940" height="346" alt="image" src="https://github.com/user-attachments/assets/88df690a-a4e1-4000-970f-ae9f657b8645" />


---

### IDS Alert Detection

<img width="940" height="893" alt="image" src="https://github.com/user-attachments/assets/6c42f28c-b993-4752-8689-275088164b84" />
<img width="250" height="92" alt="image" src="https://github.com/user-attachments/assets/c783f0c7-9364-41a9-93fe-2938d876a41e" />


---

### Wireshark Packet Capture

<img width="940" height="718" alt="image" src="https://github.com/user-attachments/assets/3cd51f51-0773-4e5b-8312-92185937011b" />


---

### Alert Log Output

<img width="940" height="146" alt="image" src="https://github.com/user-attachments/assets/a6001f21-9577-4420-b004-e2c4594be636" />
<img width="940" height="660" alt="image" src="https://github.com/user-attachments/assets/a23b7791-ad9f-4e5a-b0a8-f526ea0dba5f" />




