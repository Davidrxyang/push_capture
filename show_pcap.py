from scapy.all import rdpcap

def show_pcap_contents(pcap_file):
    packets = rdpcap(pcap_file)
    for i, pkt in enumerate(packets):
        print(f"Packet {i+1}:")
        pkt.show()
        print("-" * 40)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python show_pcap.py <pcap_file>")
    else:
        show_pcap_contents(sys.argv[1])