import math
import json
import itertools
from collections import defaultdict


lowers = [chr(ord('a') + i) for i in range(26)]
uppers = [chr(ord('A') + i) for i in range(26)]


def chmov(ch, k2=0, k1=1, use_digit=True):
    if ch.isalpha():
        st = ord('A') if ch.isupper() else ord('a')
        mod = 26
    elif use_digit and ch.isdigit():
        st = ord('0')
        mod = 10
    else:
        return ch
    return chr((k1 * (ord(ch)-st) + k2) % mod + st)


def mappings(it1, it2):
    if len(it1) > len(it2):
        permut = itertools.permutations(it1, len(it2))
    else:
        permut = itertools.permutations(it2, len(it1))
    for p in permut:
        zipped = zip(p,it2) if len(it1) > len(it2) else zip(it1, p)
        yield zipped


def dicontra(dic1, dic2):
    both = dic1.keys() & dic2.keys()
    contra = [k for k in both if dic1[k] != dic2[k]]
    return contra


def dicmax(dic):
    return max(dic, key=dic.get)


def dicsort(dic, descending=True, by='value'):
    by = 1 if by != 'key' else 0
    return {k: v for k, v in sorted(dic.items(), key=lambda x: x[by], reverse=descending)}


def entropy(data):
    probs = [data.count(x)/len(data) for x in data]
    ans = [-p * math.log2(p) for p in probs]
    return sum(ans)


def freqnt(s: str, alonly=True, descending=True, order=1):
    k = order
    if k == 1:
        dic = {ch: s.count(ch)/len(s) for ch in s if not alonly or ch.isalpha()}
    else:
        dic = {s[i:i+k]: s.count(s[i:i+k])/len(s) for i in range(len(s)-k) if not alonly or s[i:i+k].isalpha()}
    return dicsort(dic) if descending else dic


def IC(s):
    ans = sum([s.count(ch)*(s.count(ch)-1) for ch in lowers])
    ans /= len(s)*(len(s)-1)
    return ans


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def inv(a, m):
    if gcd(a, m) != 1:
        return None
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3 != 0:
        q = u3 // v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1 % m


def streplace(s, dic, missing=None, apply=lambda x: x):
    '''when x not in dic, use default value or apply func'''
    return ''.join([dic.get(x, missing or apply(x)) for x in s])


def str2col(s, i, index=None):
    s = list(s)
    cols = [''.join(map(lambda x: s[x], filter(lambda x: x % i == j, range(len(s))))) for j in range(i)]
    return cols if index is None else cols[index]


def strix(s, colen):
    return [s[i:i+colen] for i in range(0,len(s),colen)]


def wordpat(w):
    i, dic, lst = 0, {}, []
    for ch in w:
        try:
            x = dic[ch]
        except KeyError:
            dic[ch] = x = i
            i += 1
        lst.append(x)
    return '.'.join([str(x) for x in lst])


if __name__ == '__main__':
    print(wordpat('hello'))
    pats = defaultdict(list)
    # with open('data/words10000.txt') as f:
        # for w in f:
            # w = w.strip()
            # pats[wordpat(w)].append(w)
    # with open('data/pats10000.py', 'w') as f:
        # json.dump(pats, f, indent=2)
    dic1 = {1: 2, 2: 4}
    dic2 = {1: 2, 3: 5}
    print(dicontra(dic1, dic2))
    print(dic1.items() <= dic2.items())

