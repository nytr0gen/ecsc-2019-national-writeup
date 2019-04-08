cnt = [
    [0 for _ in range(0, 16)]
    for _ in range(0, 64)
]

with open('Alice_replies.txt', 'r') as f:
    data = f.read().strip()

hashes = data.split("\n")
for h in hashes:
    for i, c in enumerate(h):
        c_ = int(c, 16)
        cnt[i][c_] += 1

flag = ''
for i in range(0, 64):
    possible = []
    for j, c in enumerate(cnt[i]):
        if i < 32 and c == 1:
            possible.append(j)
        elif i >= 32 and c == 0:
            possible.append(j)

    print("#%d: %s" % (i, repr(possible)))
    flag += '%x' % possible[0]

print("ECSC{%s}" % flag)
