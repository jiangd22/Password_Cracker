import numbers
import string
import itertools
import hashlib

with open("/Users/davidjiang/Info_sec/lab3/salt.txt", "r") as f:
  salt = f.read().strip()

hashes = []
with open("/Users/davidjiang/Info_sec/lab3/hashes.txt", "r") as f:
  for line in f:
    # strip new line character
    hash = line.strip()
    hashes.append(hash)

# char + num list
list = []
for i in range(0,26):
    list.append(chr(97+i))
# numbers list
for i in range(0,10):
    list.append(str(i))

# symbols list !@#$%^&*-+=<>?
list.append('!')
list.append('@')
list.append('#')
list.append('$')
list.append('%')
list.append('^')
list.append('&')
list.append('*')
list.append('-')
list.append('+')
list.append('=')
list.append('<')
list.append('>')
list.append('?')

for i in range(1, 5):
    for bruteForce in itertools.product(list, repeat=i):
        bruteForce = ''.join(bruteForce)
        salted_password = (salt + bruteForce).encode('utf-8')
        hash_value = hashlib.sha256(salted_password).hexdigest()
        if hash_value in hashes:
            print(hash_value,":", bruteForce)
