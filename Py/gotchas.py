"""
python's closures are late binding
values of variables used in closures are looked up at the time the inner function is called
"""


def create_multipliers():
    return [lambda x: i * x for i in range(5)]


for multiplier in create_multipliers():
    print(multiplier(2))


# not limited to lambda
def create_multipliers():
    multipliers = []
    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)
    print(f"i={i}")
    return multipliers


for multiplier in create_multipliers():
    print(multiplier(2))


def create_multipliers():
    return [lambda x, i=i: i * x for i in range(5)]


for multiplier in create_multipliers():
    print(multiplier(2))
