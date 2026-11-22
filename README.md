# CSA07 Assignment 5 - Computer Networks (CO5)

Name: Sai Ramanesh
Register number: 1912260298
OS: macOS 15.4.1
Python: 3.14.0
Tools: Python 3, Wireshark / Packet Tracer / iperf3 (not used for the submitted programs)

## Programs

| Task | Folder | Program | Screenshot |
|---|---|---|---|
| A4 - Stateful firewall | `A4/` | `A4/A4_stateful_firewall.py` | `screenshots/CO5_A4_Stateful_Firewall.png` |
| B1 - VoIP quality metrics | `B1/` | `B1/B1_voip_metrics.py` | `screenshots/CO5_B1_VoIP_Metrics.png` |

Each folder contains the Python program and the captured `output.txt`.

## How to run

    python3 A4/A4_stateful_firewall.py
    python3 B1/B1_voip_metrics.py

## Results

- A4: inside-to-outside traffic is allowed, matching replies are allowed, unsolicited outside traffic is denied, and a reply to a host that never sent a packet is denied. The output matches the expected result.
- B1: packet loss 16.7%, average delay 49.8 ms, jitter 2.80 ms, R-factor 53.4, MOS 2.75, VoIP quality `poor`. The output matches the expected result.

## Notes

The PDF provides Complete-the-Code programs only for A4 (stateful firewall) and B1 (VoIP metrics). A1, A2, A3, A5, B2, B3 and B4 are calculation, written-analysis, Wireshark or simulation tasks and have no Python program in the PDF.
