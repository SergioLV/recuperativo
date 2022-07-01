import secrets
import sys
def enc(message, key):
    xor = []
    aux = ""
    ascii_message = [ord(a) for a in message]
    ascii_key = len(key)
    for i in ascii_message:
        xor.append(i ^ ascii_key)
    for ascii in xor:
        aux += ascii.to_bytes((ascii.bit_length() + 7) // 8,'big').decode()
    return aux

def dec(message, key):
    decrypted = []
    aux = ""
    for letter in message:
        decrypted.append(ord(letter) ^ len(key))
    for dec in decrypted:
        aux += dec.to_bytes((dec.bit_length() + 7) // 8,'big').decode()
    return aux   

def symmetricEncryption(argv):
    try:
        option = argv[1]
    except(NameError, IndexError):
        print("Missing parameter after flag.")
    if(option == "-e"):
        try:
            message = argv[2]
            key = argv[3]
            encripted_message = enc(message, key)
            print(encripted_message)
        except(NameError, IndexError):
            print("Missing parameter after flag.")
    
    if(option == "-d"):
        try:
            message = argv[2]
            key = argv[3]
            plain_text = dec(message, key)
            print(plain_text)
        except(NameError, IndexError):
            print("Missing parameter after flag.")

if __name__ == '__main__':
    symmetricEncryption(sys.argv)
    