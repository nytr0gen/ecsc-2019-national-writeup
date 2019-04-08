from pwn import *
import sys
import time


program_name = './a.out'

remote_server = '37.128.230.46'
PORT = 50021
if __name__ == "__main__":
    p = process(program_name)

    data = p.recvline()
    log.info(data)
    p.sendline('a')
    data = p.recvline()
    log.info(data)
    p.sendline('a')

    data = p.recvuntil('Try harder :(')
    log.info(data)
    answer = int(data.split('The answer was: ')[1].split('.')[0])

    p = remote(remote_server, PORT)
    
    data = p.recvline()
    log.info(data)
    p.sendline('a')
    data = p.recvline()
    log.info(data)
    p.sendline(str(answer))

    data = p.recvline()
    log.info(data)
    data = p.recvline()
    log.info(data)

