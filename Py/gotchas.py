def create_multipliers():
    return [lambda x: i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))

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
    return [lambda x, i=i : i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))
