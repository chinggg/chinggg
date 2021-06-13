import math


def entropy(data):
    probs = [data.count(x)/len(data) for x in data]
    ans = [-p*math.log2(p) for p in probs]
    return sum(ans)


data = ''.join([chr(x) for x in range(65, 91)])
print(data, entropy(data))
data = 'A'*26
print(data, entropy(data))
s = input("Input: ")
print(entropy(s))
