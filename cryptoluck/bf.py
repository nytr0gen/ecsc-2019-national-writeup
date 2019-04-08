#!/usr/bin/env python2
from pwn import *
import hashlib
import re
import time
import itertools

def check(h, key):
    return h[0:6] == key

def hash(s, cipher):
    if cipher == 'sha1':
        return hashlib.sha1(s).hexdigest()
    elif cipher == 'sha224':
        return hashlib.sha224(s).hexdigest()
    elif cipher == 'sha256':
        return hashlib.sha256(s).hexdigest()
    elif cipher == 'sha384':
        return hashlib.sha384(s).hexdigest()
    elif cipher == 'sha512':
        return hashlib.sha512(s).hexdigest()
    elif cipher == 'md5':
        return hashlib.md5(s).hexdigest()

    raise ValueError('cipher not found %s' % cipher)

def break_hash(cipher, key):
    for i in xrange(0, 256**4):
        s = str(i)
        h = hash(s, cipher)
        if check(h, key):
            print "%s(%s) = %s" % (cipher, s, h)
            return s
        elif i & 1048575 == 1048575:
            log.info('try at %s' % s)

    raise ValueError('matching hash not found')

cipher = 'sha1'
while True:
    # nc 37.128.230.46 50041
    io = remote('37.128.230.46', 50041)

    i = 0
    while True:
        time.sleep(0.2)
        data = io.recv().strip()

        # sha1.hexdigest()[0:6]
        key = data[0:6]

        log.info(data)
        log.info('key = %s' % key)

        x = break_hash(cipher, key)
        io.sendline(x)

        i += 1
        log.info("count = %d" % i)

        # time.sleep(0.1)
        # data = io.recv().strip()
        # log.info(data)

    io.interactive()
