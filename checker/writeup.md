looked around with radare2. not a classic binary

gdb all the way. saw something about PKG in registers. I thought of packers. did binwalk. lots of archives

it prints "I do not know".

```
grep -r 'do not know'
Binary file _checker.extracted/B493 matches
```

looks like python. searching for python packers. something about pyinstaller on google. let's try it.

i first tried the version for python 2. which didn't work. then by looking through `checker` i figured out that it must be python3 and it surely is PyInstaller. (some paths in the archives clearly show it)

so i tried again with the version for python3. the archive visualiser worked. extracted 1 (which I already extracted with binwalk, but now I was sure)

tried uncompyle6. didn't work. found some website. `https://python-decompiler.com/`. hell yeah

```
username = decode(decode(decode(rot13(('').join(map(str, username))))))
password = str.encode(decode(decode(rot13(unquote(decode(('').join(map(str, password))))))))
print('ECSC{%s}' % hashlib.sha256(('%s:%s' % (username, password)).encode('utf8')).hexdigest())
password = md5_to_hex(md5(password))
print('ECSC{%s}' % hashlib.sha256(('%s:%s' % (username, password)).encode('utf8')).hexdigest())
```

it was the second one

ECSC{79e17ba7189bc35bcaca6b8bcc263f8a7ed672ada400be4394fa7aad74e3af08}
