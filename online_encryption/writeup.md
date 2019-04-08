downloaded file

looked through it with wireshark

too much data. filtered by http

saw some requests. looked for POST request

got `UlBGUHtxcTU0NXNvczEyc3E2MDhxbm44cDIwMXM1MHM5NXA4NTIwb3JwOXM3NDRuMzU3M28xcXAwb3A1M3ByMDE5NzI2fQ==`

rot13(b64decode())

```
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)ROT13(true,true,13)&input=VWxCR1VIdHhjVFUwTlhOdmN6RXljM0UyTURoeGJtNDRjREl3TVhNMU1ITTVOWEE0TlRJd2IzSndPWE0zTkRSdU16VTNNMjh4Y1hBd2IzQTFNM0J5TURFNU56STJmUT09
```


ECSC{dd545fbf12fd608daa8c201f50f95c8520bec9f744a3573b1dc0bc53ce019726}
