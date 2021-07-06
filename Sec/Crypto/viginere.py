import re
import pprint
import statistics
from utils import chmov
from utils import dicsort
from utils import freqnt
from utils import IC
from utils import lowers
from utils import str2col


ENGIC = 0.0667
REJECT = re.compile(r'[^a-z]')
FREQ = [0.0855,0.016,0.0316,0.0387,0.121,0.0218,0.0209,0.0496,0.0733,0.0022,0.0081,0.0421,0.0253,0.0717,0.0747,0.0207,0.001,0.0633,0.0673,0.0894,0.0268,0.0106,0.0183,0.0019,0.0172,0.0011]
FREQ = {ch: x for ch, x in zip(lowers, FREQ)}


def preprocess(s):
    s = s.lower()
    return REJECT.sub(r'', s)


def encrypt(msg, key):
    k, st = len(key), ord('a')
    j, lst = 0, []
    for i, ch in enumerate(msg):
        if ch.isalpha():
            lst.append(chmov(ch, ord(key[j % k]) - st))
            j += 1
        else:
            lst.append(ch)
    return ''.join(lst)


def decrypt(c, key):
    k, st = len(key), ord('a')
    j, lst = 0, []
    for i, ch in enumerate(c):
        if ch.isalpha():
            lst.append(chmov(ch, st - ord(key[j % k])))
            j += 1
        else:
            lst.append(ch)
    return ''.join(lst)


def guesize(s, low=2, high=10):
    ICs = {}
    ICavr = {}
    ICstd = {}
    for k in range(low, high):
        ICs[k] = [IC(s[i::k]) for i in range(k)]
        ICavr[k] = sum(ICs[k])/k
        ICstd[k] = statistics.stdev(ICs[k])
    ans1 = dicsort(ICstd, descending=False)
    ans2 = {k: v for k, v in sorted(ICavr.items(), key=lambda x: abs(x[1]-ENGIC))}
    # ans3 = {k: max(max(ICs[k])-ICavr[k], ICavr[k]-min(ICs[k]))/k for k in ICavr}
    # print("ICs:", ICs)
    # print("IC stdev:", ans1)
    print("IC avr sorted:", ans2)
    return ans2 #.keys()


def crack(s, sizes):
    while True:
        try:
            size = int(input('choose key size:'))
        except:
            break
        keychs = []
        for blk in str2col(c, size):
            freq = freqnt(blk)
            pseudo = {offset: sum([freq[k] * FREQ[chmov(k, offset)] for k in freq]) for offset in range(1,26)}
            pseudo = sorted(pseudo.items(), key=lambda x: abs(x[1] - ENGIC))
            keychs.append(chmov('a', -pseudo[0][0]))
        guekey = ''.join(keychs)
        print('guess key:', guekey)
        print('guess msg:', decrypt(c, guekey))


if __name__ == '__main__':
    msg = """To be, or not to be, that is the question—
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
And by opposing end them?
William Shakespeare - Hamlet"""
    key = 'english'
    c = encrypt(preprocess(msg), key)
    print(c)
    sizes = guesize(c)
    crack(c, sizes)
    print('answer:', decrypt(c, key))
