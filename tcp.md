# TCPdump

make sure you have tcpdump setup!

## reading a pcap file

use the included pcap content reading tool to read a pcap file:
`python show_pcap.py PCAP_FILE_NAME.pcap`

## capturing packets

`sudo tcpdump -i any tcp port 5223 -w apns.pcap`

capture packets from apple APN service and dumps into apns.pcap file
