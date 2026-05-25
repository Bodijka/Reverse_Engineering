def f(x):
    return x & 0xFFFFFFFF


x = 0x7AA5F10B
y = 0x14994376
z = 0xB9487CF2
n = 0xA3A

magic = 0x94E


for i in range(n):
    a = f(x ^ 0x91D379B4)
    b = f(a ^ f(z + 0x66852A4E))

    c = f(b + 0x42CAD70E)

    d = f(a + 0x53F3BF76)
    e = f(d ^ (b >> 3))

    z2 = f((f(e - magic) ^ b) - 0x5116FF8F)
    y2 = f(f((y ^ 0x9F563735) - e) ^ magic)
    x2 = f(c ^ y2)

    x = x2
    y = y2
    z = z2


print("%08X-%08X-%08X-%08X" % (x, y, z, n))