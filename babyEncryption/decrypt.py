import string

all_lines = ''
with open('msg.enc','r') as file:
    for line in file:
        all_lines += line
ct = bytes.fromhex(all_lines)
word = ''
for byte in ct:
    number = int(byte)
    for ascii_car in range(128):
        if(((123 * ascii_car + 18) % 256) == number):
            word += chr(ascii_car)
            
print(word)



