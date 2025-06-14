# push_capture
capturing push notification TCP packets on the network for analysis

## usage

## TCPdump

make sure you have tcpdump setup!

## reading a pcap file

use the included pcap content reading tool to read a pcap file:
`python show_pcap.py PCAP_FILE_NAME.pcap`

## send a test push notification 

when I get a chance, I will set up an actual push notification testing setup

on the apple ecosystem, this requires me to set up developer tools and get certificates and a bunch of other fun things

## APPLE - APNs

`sudo tcpdump -i any tcp port 5223 -w apns.pcap`

capture packets from apple APN service and dumps into apns.pcap file

APNs notifications are sent to port 5223

Apple address block

ipv4:

17.249.0.0/16

17.252.0.0/16

17.57.144.0/22

17.188.128.0/18

17.188.20.0/23

ipv6:

2620:149:a44::/48

2403:300:a42::/48

2403:300:a51::/48

2a01:b740:a42::/48