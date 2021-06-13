#!/usr/bin/python3
import os
import crypt

FILE = '/etc/shadow'
DICT = 'dictionary.txt'

with open(DICT) as f:
    pwds = f.read().splitlines()

ans = []
with open(FILE) as f:
    for x in f:
        try:
            name, secret, *_  = x.split(':')
            if '$' not in secret:
                continue
            salt = secret[:secret.rfind('$')]
            for p in pwds:
                q = crypt.crypt(p, salt)
                if q == secret:
                    ans.append((name,p))
                    break
        except ValueError:
            pass

print(ans)
