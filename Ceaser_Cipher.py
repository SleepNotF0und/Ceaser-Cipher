while True:
    ch=int(input("""\n
==========================
| 1-Encrypt   2-Decrypt  |
==========================\n"""))
    if ch == 1:
        text = input("text:")
        print("!!! KEY MUST BE NUMBER !!!\n")
        shift = int(input("Key :"))
        print("\n!!Encrypted!!\n")
        for x in text: 
            alpha = ord(x)+shift
            if alpha > ord('z'):
                alpha -=26
            print("Text:",chr(alpha),end="")

    elif ch == 2:
        text=input("text:")
        shift = int(input("Key :"))
        print("\n!!Decrypted!!\n")
        for x in text: 
            alpha = ord(x)-shift
            if alpha < ord('a'):
                alpha += 26
            print("Text:",chr(alpha),end="")
