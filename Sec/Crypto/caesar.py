def chmov(ch, k2=0, k1=1):
    if ch.isupper():
        st = ord('A')
    elif ch.islower():
        st = ord('a')
    else:
        return ch
    return chr((k1 * (ord(ch)-st) + k2)%26 + st)

def encrypt(m, k):
    res = ''.join([chmov(ch, k) for ch in m])
    return res

def decrypt(c, k=None):
    if k is None:
        res = [(k, encrypt(c, -k)) for k in range(26)]
    else:
        res = ''.join([chmov(ch, -k) for ch in c])
    return res

if __name__ == '__main__':
    message = 'flag_is_520'
    enword = encrypt(message, 3)
    print(enword)
    print(decrypt(enword))
    print(decrypt(enword, 3))
