


looked through with wireshark. found some html. man page from ncat and one bin. packet by packet extracted bin. tedious. it was netcat binary...

looked at icmp. apparently icmp can send data and the server sends it back. more than 10 packets, how do we automate this?

enter tshark

```
tshark -r captura.pcapng -e data -Tfields '(icmp) && (ip.src == 10.10.10.1)' > data.hex
cat data.hex| xxd -r -p > img.png
```


got the img

```
username admin password 7 03217838251474481E0D4D5144440A08532F7B732C666675465E425B0052080B040058051D44000000525302520F0C57550E53021702500C0A050A254A1650405542135B0D5037
```

didn't know what that is. searched google for '142 char password'. nothing. searched for `username admin password 7`. got something about cisco. searched `cisco password cracker`

http://www.ifm.net.nz/cookbooks/passwordcracker.html

got flag

```
ECSC{5d0d4436ad7e07d5375948ad13746fe2987aa7fd7126dfdd47acedf89905a0a4}
```
