# Lab 1 - Wireshark
This lab focuses on capturing and analyzing network traffic using Wireshark. It includes analyzing TCP and UDP packets and comparing their characteristics.

## Part 1: Capturing and Analyzing 
### HTTP Packet Filtering
I used the HTTP filter in Wireshark to display only HTTP packets from the captured network traffic.
<img width="700" alt="image" src="https://github.com/user-attachments/assets/ca7aff54-e509-4783-affd-824057642847" />

## Part 2: Analyzing TCP Traffic
### Following the TCP Stream
I used Follow TCP Stream to view the complete communication between the client and the server, including the HTTP request and response.

<img width="700"  alt="image" src="https://github.com/user-attachments/assets/a94d80b0-dce4-4a56-93c5-709361d9e8d0" />

### TCP Three-Way Handshake
The TCP connection establishment was observed using the SYN, SYN-ACK, and ACK packets. These packets show the three-way handshake used to establish a TCP connection.
<img width="700" alt="image" src="https://github.com/user-attachments/assets/bc649d94-a0c7-401a-b4ea-795e334a2711" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/b773ba58-cabe-4aa0-bc49-427c3c231a83" />

### TCP Data Transfer
I used the tcp.len > 0 filter to display TCP packets that contain data and observed the packet length and TCP flags.
<img width="700" alt="image" src="https://github.com/user-attachments/assets/78e2b499-c229-4a8f-846a-e31b2121e745" />

## Part 3: Capturing and Analyzing UDP Traffic
### UDP Packet Filtering and Analysis
I used the UDP filter in Wireshark to display UDP packets from the captured traffic. I selected a UDP packet and observed its source port, destination port, length, checksum, and payload.
<img width="700" alt="image" src="https://github.com/user-attachments/assets/c274db74-ed5f-4855-be2e-26d5eaa6c86c" />
<img width="700" alt="image" src="https://github.com/user-attachments/assets/e50a26dd-e637-423f-b0fd-3d2b34a37c5f" />

## Part 4: Comparing TCP and UDP
### TCP and UDP Comparison
I compared TCP and UDP in terms of reliability, connection establishment, data integrity, use cases, and performance.
<img width="700" alt="image" src="https://github.com/user-attachments/assets/3b120ed7-9db1-4287-a1d4-8ac739d24533" />

## link word document :
[Lab1.docx](https://github.com/user-attachments/files/32391429/Lab1.docx)
