from scapy.all import rdpcap

def show_pcap_contents(pcap_file):
    txt_file = pcap_file.rsplit('.', 1)[0] + '.txt'
    with open(txt_file, 'w') as f:
        packets = rdpcap(pcap_file)
        for i, pkt in enumerate(packets):
            f.write(f"Packet {i+1}:\n")
            f.write(pkt.show(dump=True))
            f.write("\n" + "-" * 40 + "\n")
    print(f"Results saved to {txt_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python print_pcap.py <pcap_file>")
    else:
        show_pcap_contents(sys.argv[1])