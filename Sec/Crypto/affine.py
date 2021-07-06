from utils import chmov
from utils import gcd
from utils import inv


def encrypt(m, k2, k1=1, use_digit=True):
    """pre: gcd(k1,26)=1"""
    res = ''.join([chmov(ch, k2, k1, use_digit) for ch in m])
    return res


def decrypt(c, k2=None, k1=1, use_digit=False):
    """pre: gcd(k1,26)=1"""
    if k2 is None:
        return brute_force(c)
    elif gcd(k1, 26) != 1:
        return None
    res = ''.join([chmov(ch, -k2*inv(k1, 26), inv(k1, 26), use_digit) if ch.isalpha()
            else chmov(ch, -k2*inv(k1, 10), inv(k1, 10), use_digit) if ch.isdigit()
            else ch for ch in c])
    return res


def brute_force(c):
    return ([decrypt(c,i,1) for i in range(26)] ,[decrypt(c,j,i) for i in range(1,26) if gcd(i, 26) == 1 for j in range(26)])


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
    print([m for m in guess2 if 'flag' in m])
