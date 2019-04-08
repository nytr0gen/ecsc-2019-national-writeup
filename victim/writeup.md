looked at http

then ftp.

then randomly with strings. saw something interesting.

```
ip.src == 10.1.10.71 or ip.dst == 10.1.10.71 and data
```

found some files. `indecisive.jpg`, some `txt` files and `log.zip`

zip file

```
➜ victim unzip log.zip
Archive:  log.zip
   skipping: Flag.txt                unsupported compression method 99
```

googleing around it says i can use `7z`. but 7z asks for password.

remembering the description `some authentication information will help you to capture the flag`

```
strings file.pcap| grep PASS
```

password `VADPRDqid4TaB0r5a2B0n9wLp` worked

ECSC{AC0DFD65CA16813A6AD68C4BA55F8C607496D93E2408EE0B5EF6F1B9ACCE0BC9}
