from Crypto.Cipher import ChaCha20

import os


def encryptMessage(message, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(message)
    return ciphertext


if __name__ == "__main__":
    message = b"Our counter agencies have intercepted your messages and a lot "
    message += b"of your agent's identities have been exposed. In a matter of "
    message += b"days all of them will be captured"

    from_hex = bytes.fromhex('c4a66edfe80227b4fa24d431')
    e_key = 0
    for key in range(2 ** 32):
        if (key % 1000000 == 0):
            print(key)
        b_key = key.to_bytes(32, byteorder='big')

        if encryptMessage(message, b_key,
                          from_hex).hex() == '7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990':
            print("Key found and its: ")
            e_key = key
            break
    print(e_key)




