def main():
    s = bytearray(b'bcjac --- YnuNmQPGhQWqCXGUxuXnFVqrUVCUMhQdaHuCIrbDIcUqnKxbPORYTzVCDBlmAqtKnEJcpED --- UVQR')

    k1, s, k2 = s.split(b' --- ')

    for i in range(len(s)):
        c = s[i]
        if 65 <= c <= ord('Z'):
            c = 65 + ((c - 65) - 2) % 26
        else:
            c = 97 + ((c - 97) - 9) % 26
        s[i] = c

    print(s)

if __name__ == '__main__':
    main()
