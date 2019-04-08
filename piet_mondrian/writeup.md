downloaded

checked stegsolve, strings and some others

run binwalk. see some pngs.

```
binwalk -D 'png image:png' piet.jpg
```

got the pngs. no idea what now. searched for piet and secret online. found https://www.bertnase.de/npiet/ . followed hint from that page and used gimp

got flag


```
➜ piet_mondrian ./pkg/usr/bin/npiet ./p1.png | head -c 30
ECSC{e647c19e4fc7838bf7ECSC{e6%                                                               ➜ piet_mondrian ./pkg/usr/bin/npiet ./p2.png | head -c 30
64abbdcb0c1f08adca163cd64abbdc%                                                               ➜ piet_mondrian ./pkg/usr/bin/npiet ./p3.png | head -c 30
adfb889bee5201fc4397e5d}adfb88%
```

ECSC{e647c19e4fc7838bf764abbdcb0c1f08adca163cdadfb889bee5201fc4397e5d}
