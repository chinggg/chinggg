def ch_move(ch, k2=0, k1=1, use_digit=True):
    if ch.isalpha():
        st = ord('A') if ch.isupper() else ord('a')
        mod = 26
    elif use_digit and ch.isdigit():
        st = ord('0')
        mod = 10
    else:
        return ch
    return chr((k1 * (ord(ch)-st) + k2) % mod + st)


def gcd(a, b):
    return a if b==0 else gcd(b, a%b)


def inv(a, m):
    if gcd(a, m)!=1:
        return None
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3 != 0:
        q = u3 // v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m


def encrypt(m, k2, k1=1, use_digit=True):
    """pre: gcd(k1,26)=1"""
    res = ''.join([ch_move(ch, k2, k1, use_digit) for ch in m])
    return res


def decrypt(c, k2=None, k1=1, use_digit=False):
    """pre: gcd(k1,26)=1"""
    if k2 is None:
        return brute_force(c)
    elif gcd(k1, 26) != 1:
        return None
    res = ''.join([ch_move(ch, -k2*inv(k1,26), inv(k1,26), use_digit) if ch.isalpha()
            else ch_move(ch, -k2*inv(k1,10), inv(k1,10), use_digit) if ch.isdigit()
            else ch for ch in c])
    return res


def brute_force(c):
    return ([decrypt(c,i,1) for i in range(26)] ,[decrypt(c,j,i) for i in range(1,26) if gcd(i,26) == 1 for j in range(26)])


if __name__ == '__main__':
    message = 'flag{ABC123xyz789}'
    print(message)
    enword = encrypt(message, 3, use_digit=False)
    print("移位, k=3, 不加密数字", enword)
    deword = decrypt(enword, 3, use_digit=False)
    print(deword)
    enword = encrypt(message, 2, 3)
    print("仿射, k1=3, k2=2", enword)
    deword = decrypt(enword, k2=2, k1=3)
    print(deword)
    enword = 'gkhl{nbkrzpb_yz_ryg_nzokw_yqvt_vt_hggvub_rxeqbo}'
    guess1, guess2 = brute_force(enword)
    print("爆破移位", guess1)
    print("爆破仿射", guess2)
    print([m for m in guess2 if m.startswith('flag')])
