import string

def encryption(msg):
    ct = []
    for char in msg:
        print((123 * ord(char) + 18) % 256)
        ct.append((123 * ord(char) + 18) % 256)
    return bytes(ct)

ct = encryption("This is best day of my life!")
f = open('./msg1.enc','w')
f.write(ct.hex())
f.close()


