# intercepting and decrypting packets with mitmproxy 

set up mitmproxy! (follow instructions on mitmproxy.org)

## setup 

we should not be running mitmproxy on public networks, lets make sure we are restricting it to our own network with devices we own. 

### structure

Phone -> Wifi -> Laptop

Phone and laptop are connected to the same wifi network (which we own, presumably)

### setup manual proxy

setup the internet proxy manually for the wifi network on the phone device 

- set the host to your laptops IP address

(on laptop)
```
ip addr show 
```

- set the port to 8080

- Note: setting the proxy in network settings does not force app providers to obey the proxy. WIP. 

### activate mitmproxy 

```
mitmproxy --mode regular --listen-host <laptop-ip> --listen-port 8080
```

this will activate an interactive terminal interface on the laptop

### install mitm certificate on phone 

go to mitm.it, download android certificate, install on device

-> now we are capturing traffic!

TODO: automate some of this stuff with scripts? be very careful with ip addresses ... 

