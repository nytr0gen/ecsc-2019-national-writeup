got pcap. searched with wireshark. too much data.

```
strings challenge.pcapng
```

scrolled through it until I found something interesting. found some `gcellid` and Paris. googled for global cell id. found this website `https://cellidfinder.com/mcc-mnc`, searched for france - MCC 208. `strings challenge.pcapng | grep 208`

used `https://opencellid.org/` with
```
{'INFO_CELL_GLOBAL_ID': {'sector': 2, 'cell_id': 1106, 'cell_gid': u'208f2075ee4025', 'bts': 69, 'mcc': 208, 'lac': 22510, 'mnc': 20}}
```

got to city of Lanton, France. `https://en.wikipedia.org/wiki/Lanton,_Gironde`

```
INSEE/Postal code
33229 /33138
```

wasn't sure which. tested both

ECSC{50fb4a9bee63b51141c2b32e42251d1f88104731d1a7b73ff9750626227d7f5a}
