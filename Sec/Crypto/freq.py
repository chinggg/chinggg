import json
from utils import dicmax
from utils import dicontra
from utils import dicsort
from utils import freqnt
from utils import lowers # list
from utils import streplace
from utils import wordpat
from utils import mappings
from data.pats10000 import ALLPATS


FILE = 'data/ciphertext.txt'
FREQ = [0.0855,0.016,0.0316,0.0387,0.121,0.0218,0.0209,0.0496,0.0733,0.0022,0.0081,0.0421,0.0253,0.0717,0.0747,0.0207,0.001,0.0633,0.0673,0.0894,0.0268,0.0106,0.0183,0.0019,0.0172,0.0011]
FREQ = {ch: x for ch, x in zip(lowers, FREQ)}
print(FREQ)
FREQ = dicsort(FREQ)
with open('data/words10000.txt') as f:
    WORDS = {w for w in f.read().split()}


class Freqracker():
    def __init__(self, s, mode='freq'):
        self.raw = s.strip()
        self.words = set(s.split())
        self.words = {w: s.count(w) for w in self.words}
        self.words = dicsort(self.words)
        self.freq = freqnt(s, order=1)
        self.tb = {}
        self.score = 0
        self.mode = mode

    def __str__(self):
        missing = set(lowers) - set(self.tb.keys())
        missing = '\n' + str(missing) if missing else '\n'
        return self.ans.strip() + '\n' + str(dicsort(self.tb, by='key', descending=False)) + str(missing)

    def __call__(self):
        if self.mode == 'freq':
            self.freqinit()
            self.adjust()
        else:
            self.patinit()
            print(len(self.tb), "letters have done after patinit")
            self.complete()
        func = lambda x: x.upper() if x.isalpha() else x
        self.ans = streplace(self.raw, self.tb, apply=func)
        print(self)

    def grade(self, tb=None):
        ''' sum of words' count in text'''
        tb = tb or self.tb
        finds = {k: v for k, v in self.words.items() if streplace(k, tb, '_') in WORDS}
        score = sum(finds.values()) / len(self.words)
        return score

    def consider(self, dic):
        '''determine if dic should be added by grading'''
        newtb = self.tb | dic
        if (newscore := self.grade(newtb)) > self.score:
            self.tb = newtb
            self.score = newscore
            print("Unsafe merge! Score =", self.score)

    def erase(self, keys):
        '''used when found conflicting keys'''
        print("Erase conflicting letters:", keys)
        for k in keys:
            del self.tb[k]

    def merge(self, dic):
        '''pre: no conflict with tb'''
        self.tb.update(dic)
        self.score = self.grade()
        print("Safe merge! Score =", self.score)

    def freqinit(self):
        '''init full tb by frequency'''
        std = FREQ.copy()
        freq = self.freq.copy()
        while True:
            try:
                k, v = dicmax(freq), dicmax(std)
            except ValueError:
                break
            self.tb[k] = v
            print('pair:', k, v)
            del freq[k], std[v]

    def adjust(self, thresh=20):
        ''' adjust tb by mappings from long patterns'''
        # words = sorted(self.words.keys(), key=len, reverse=True)
        words = filter(lambda x: len(x) > 5, self.words.keys())
        for w in words:
            try:
                cans = ALLPATS[wordpat(w)]
                if len(cans) == 1:
                    can = cans[0]
                    dic = {k: v for k, v in zip(w, can)}
                    self.consider(dic)
                else:
                    if thresh and len(cans) > thresh:
                        continue
                    for can in cans:
                        dic = {k: v for k, v in zip(w, can)}
                        self.consider(dic)
            except KeyError:
                pass

    def patinit(self, thresh=30):
        '''use patterns to init credible mappings'''
        for w in self.words:
            try:
                cans = ALLPATS[wordpat(w)]
                if len(cans) == 1:
                    can = cans[0]
                    dic = {k: v for k, v in zip(w, can)}
                    kontra = dicontra(self.tb, dic)
                    if not kontra:
                        self.merge(dic) if not dic.items() <= self.tb.items() else None
                    else:
                        # self.erase(kontra)
                        self.consider(dic)
                else:
                    if thresh and len(cans) > thresh:
                        continue
                    for can in cans:
                        dic = {k: v for k, v in zip(w, can)}
                        kontra = dicontra(self.tb, dic)
                        if not kontra:
                            self.merge(dic) if not dic.items() <= self.tb.items() else None
                        # else:
                            # self.consider(dic)
            except KeyError:
                pass

    def complete(self):
        '''iter through all possible mappings in remaining letters'''
        r1 = set(lowers) - set(self.tb.keys())
        r2 = set(lowers) - set(self.tb.values())
        for mp in mappings(r1, r2):
            dic = dict(mp)
            self.consider(dic)


if __name__ == '__main__':
    with open(FILE) as f:
        s = f.read().lower()
    fq = Freqracker(s)
    # fq = Freqracker(s, mode='pat')
    fq()
    exit(0)
