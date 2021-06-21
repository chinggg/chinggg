import re


s = re.split('\.+', 'abc...def')
print(s)
s = re.split('[\.]+', 'abc...def')
print(s)

s = 'Nothing is better than tao'
pat = re.compile(r'(?:is\s)better(\sthan)')
result = pat.search(s)
print(result.span())
