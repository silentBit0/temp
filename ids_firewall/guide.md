Below is a **complete, viva-ready, end-to-end theory + practical explanation** of the entire experiment:
**IDS, HIDS, Event Correlation, Firewall & iptables** — all based exactly on your lab manual .

This is structured so that **you can answer ANY viva question** on theory, implementation, logs, SNORT, Logwatch, SEC, iptables, packet filtering, and modern cybersecurity concepts.

---

# **MASTER THEORY FOR EXPERIMENT 8 – IDS + FIREWALL**

*(Covers everything from fundamentals → tools → commands → practical → security concepts → viva answers)*
Source: Your lab file 

---

# **SECTION 1 — IDS THEORY (FOUNDATION)**

## **1. What is an Intrusion Detection System (IDS)?**

An IDS is a security mechanism that **monitors network or system activity** and detects:

* Attacks
* Scanning
* Policy violations
* Malware behavior
* Unauthorized access

An IDS does **not block** traffic (that’s IPS).
It only **detects and alerts**.

---

## **2. Two Main Types: NIDS and HIDS**

### **A. NIDS — Network Intrusion Detection System**

Monitors network traffic in real-time.

Examples:

* Snort
* Suricata

Placed at:

* DMZ
* Gateway
* Between LAN segments

Capabilities:

* Packet sniffing
* Protocol analysis
* Signature detection
* Anomaly detection

### **B. HIDS — Host-based Intrusion Detection System**

Monitors internal activities of an OS:

* System calls
* Login attempts
* File integrity
* Log files
* Application behavior

Examples:

* Logwatch
* OSSEC
* Tripwire

HIDS detects insider threats + changes inside the host.

---

# **SECTION 2 — SNORT THEORY + PRACTICAL (NIDS)**

Snort is an extremely popular **open-source NIDS/NIPS**.

Your manual details it here: 

Snort modes:

1. **Sniffer mode** – shows packets live
2. **Packet Logger mode** – stores packets
3. **NIDS mode** – detects attacks using rules

---

## **Snort Capabilities**

* Real-time traffic analysis
* Packet capturing
* Preprocessors (detect anomalies)
* Signature-based detection
* Alerts on attacks:

  * Port scans
  * OS fingerprinting
  * Buffer overflow
  * CGI attacks
  * SMB probes
  * Stealth scans

---

## **Snort Installation (Commands)**

```
sudo apt-get install snort
sudo nano /etc/snort/snort.conf
```

### **Run Snort in Sniffer Mode**

```
sudo snort -vde
```

### **Run Snort in NIDS mode**

```
sudo snort -c /etc/snort/snort.conf -q -A console
```

---

# **SECTION 3 — LOGWATCH THEORY + PRACTICAL (HIDS)**

Logwatch is a **host log analysis tool** used for HIDS.
Manual section: 

It scans logs from:

* sshd
* kernel
* cron
* systemd
* authentication logs
* mail logs

And produces human-readable reports.

---

## **Why use Logwatch?**

* Detect failed logins
* Detect brute-force attempts
* Detect root login attempts
* Collect all logs in one place
* Identify suspicious host behavior

---

## **Logwatch Commands**

Installation:

```
sudo apt-get install logwatch
```

Important usage:

```
logwatch --service sshd --range today --print
logwatch --service all --range today --print
```

Use-case from manual:

* Try SSH login attempts
* Analyze them through Logwatch

---

# **SECTION 4 — EVENT CORRELATION ANALYSIS (SEC Tool)**

Event correlation = **detect patterns in logs**.
Manual:

Example pattern:

* 3 failed logins in 1 minute → alert

SEC (Simple Event Correlator) allows rules based on:

* Regex
* Threshold
* Time window

---

## **Why Event Correlation Is Needed?**

* A single log entry ≠ attack
* Pattern of logs = attack
* Detect multi-step attacks
* Reduce false positives
* Enable automated alerts

---

## **SEC Installation**

```
sudo apt-get install sec
man sec
```

Create rule file:

```
sudo nano /etc/sec/simple_rules.conf
```

Sample rule from manual:

```
type=SingleWithThreshold
ptype=RegExp
pattern=Failed password for .*
desc=Multiple SSH Login Failures Detected
action=pipe logger -p auth.warning "SEC Alert: Multiple SSH failures detected"
window=60
threshold=3
```

Run SEC:

```
sudo sec -input=/var/log/auth.log -conf=/etc/sec/simple_rules.conf -detach
```

---

# **SECTION 5 — FIREWALL THEORY (LINUX IPTABLES)**

Manual Section:

## **What is a Firewall?**

A firewall is a packet filtering system that:

* Blocks attacks
* Enforces policy
* Protects networks
* Filters based on source/destination, port, protocol

Linux uses **iptables**.

---

## **iptables Chains**

* **INPUT** – packets coming to the host
* **OUTPUT** – packets leaving the host
* **FORWARD** – packets routed through the host

---

## **iptables Basic Commands**

### **List rules**

```
iptables -L
```

### **Clear rules**

```
iptables -F
```

### **Drop all packets**

```
iptables -A INPUT -j DROP
```

### **Allow ICMP (ping)**

```
iptables -A INPUT -p icmp -j ACCEPT
```

### **Drop all else**

```
iptables -A INPUT -j DROP
```

---

## **Blocking specific source IP**

```
iptables -A INPUT -s 192.168.56.101 -p tcp --dport 23 -j REJECT
```

---

# **SECTION 6 — ADVANCED FIREWALL RULES (MANUAL TASKS)**

### **Task 1: Drop abnormal ping (Ping of Death) and limit ICMP rate**

Ping of Death = oversized packets
Ping Flood = too many packets

Rate-limiting example:

```
iptables -A INPUT -p icmp -m limit --limit 2/second -j ACCEPT
iptables -A INPUT -p icmp -j DROP
```

---

### **Task 2: Stop bad packets**

Bad packets include:

* Invalid TCP flags
* Bad checksums
* Null packets
* Non-SYN opening connections

Example rule:

```
iptables -A INPUT -m state --state INVALID -j DROP
```

---

### **Task 3: Stop Nmap FIN/URG/PSH scan**

NMAP stealth scan uses unusual flags.
Block them:

```
iptables -A INPUT -p tcp --tcp-flags FIN,URG,PSH FIN,URG,PSH -j DROP
```

---

### **Task 4: Block Xmas Tree attack**

Xmas scan sets ALL flags:

```
iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP
```

---

### **Task 5: Block insecure protocols**

Block telnet, ftp, rsh, tftp:

```
iptables -A INPUT -p tcp --dport 23 -j DROP   # Telnet
iptables -A INPUT -p tcp --dport 21 -j DROP   # FTP
```

---

# **SECTION 7 — WINDOWS FIREWALL THEORY**

Windows Firewall provides:

* Stateful filtering
* Application-based rules
* Incoming/outgoing rules
* Pre-defined rule sets

Used to block:

* ports
* IPs
* applications

---

# **SECTION 8 — FULL VIVA THEORY**

## **1. Difference: IDS vs IPS**

IDS = detects
IPS = blocks

---

## **2. Why use SNORT?**

* Industry standard
* Open-source
* Very powerful rule engine

---

## **3. Why use HIDS?**

Detects insider attacks and file changes.

---

## **4. What is event correlation?**

Matching patterns across multiple logs.

---

## **5. Why firewall needed?**

Blocks unauthorized traffic based on rules.

---

## **6. What is iptables?**

Linux kernel firewall implementing packet filtering using netfilter framework.

---

## **7. What attacks can be detected by Snort?**

* Port scans
* Buffer overflow
* Web CGI attacks
* OS fingerprinting
* SMB probes

---

## **8. What attacks can be blocked by iptables?**

* Ping flood
* Ping of Death
* Nmap scans
* Xmas tree
* FIN scan
* Port scanning

---

## **9. SNORT rule structure**

```
action protocol srcIP srcPort -> dstIP dstPort (options)
```

---

## **10. HIDS vs NIDS**

HIDS = internal logs
NIDS = network packets

---

## **11. Why rate-limit ICMP?**

Prevent ping flood DoS.

---

## **12. What is port mirroring?**

Switch copies packets to NIDS.

---

## **13. What is a DMZ?**

A network segment exposed to the internet but isolated from internal LAN.

---

## **14. What is packet logger mode?**

Snort saves packets to disk for forensics.

---

## **15. What is log rotation?**

Periodic archival of logs to manage size.

---

# **SECTION 9 — WHAT YOU MUST SHOW IN PRACTICAL (FULL EXPECTATION)**

Manual expectations:

### **1. NIDS**

* Snort installation
* Running in 3 modes
* Generating alerts

### **2. HIDS**

* SSH attempts
* Logwatch report

### **3. Event Correlation**

* Create custom SEC rule
* Trigger events
* Show alert

### **4. Firewall**

* Show dropping ICMP
* Show allowing specific traffic
* Show blocking scans
* Show per-source IP rules
* Implement advanced conditions

---
