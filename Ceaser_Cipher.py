while True:
    ch=int(input("""\n
==========================
| 1-Encrypt   2-Decrypt  |
==========================\n"""))
    if ch == 1:
        shift = int(input("Key="))
        text = input("text:")
        print("\n!!Encrypted!!\n")
        for x in text: 
            alpha = ord(x)+shift
            if alpha > ord('z'):
                alpha -=26
            print(chr(alpha),end="")

    elif ch == 2:
        shift = int(input("Key="))
        text=input("text:")
        print("\n!!Decrypted!!\n")
        for x in text: 
            alpha = ord(x)-shift
            if alpha > ord('z'):
                alpha +=26
            print(chr(alpha),end="")