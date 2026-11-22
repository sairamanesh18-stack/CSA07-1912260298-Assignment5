"""A stateful firewall: outside packets are allowed only as replies to inside hosts."""
INSIDE = "10.5."
table = set()

def decide(src, sport, dst, dport):
    # TODO 1: If src starts with INSIDE, add (src, sport, dst, dport) to table and
    # return "allow". Otherwise return "allow" only when the reversed tuple (dst, dport,
    # src, sport) is in table, else return "deny"
    if src.startswith(INSIDE):
        table.add((src, sport, dst, dport))
        return "allow"
    if (dst, dport, src, sport) in table:
        return "allow"
    return "deny"

packets = [("10.5.1.20", 50123, "93.184.216.34", 443),
           ("93.184.216.34", 443, "10.5.1.20", 50123),
           ("185.220.1.9", 4444, "10.5.1.20", 50123),
           ("93.184.216.34", 443, "10.5.1.21", 50999),
           ("10.5.1.21", 50999, "93.184.216.34", 443),
           ("93.184.216.34", 443, "10.5.1.21", 50999)]
for src, sport, dst, dport in packets:
    print(f"{src}:{sport} -> {dst}:{dport}".ljust(44), decide(src, sport, dst, dport))
