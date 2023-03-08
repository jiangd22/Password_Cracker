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

# common passwords
common = []
hashed_common = []
with open("/Users/davidjiang/Info_sec/lab3/common.txt", "r") as f:
  for line in f:
    imput = line.strip()
    common.append(imput)

    salted_common = (salt + imput).encode('utf-8')
    hash_value = hashlib.sha256(salted_common).hexdigest()
    hashed_common.append(hash_value) 

# dictionary pawwords
dictionary = []
dictionary_upper = []
dictionary_cap = []
hashed_dictionary_lower = []
hashed_dictionary_upper = []
hashed_dictionary_capitilized = []
with open("/Users/davidjiang/Info_sec/lab3/dictionary_466550.txt", "r") as f:
  for line in f:
    imput = line.strip()
    dictionary.append(imput)
    dictionary_upper.append(imput.upper())
    dictionary_cap.append(imput.capitalize())
    
    # salt dictionary words
    salted_dictionary_lower = (salt + imput).encode('utf-8')
    salted_dictionary_upper = (salt + imput.upper()).encode('utf-8')
    salted_dictionary_capitilized = (salt + imput.capitalize()).encode('utf-8')
    
    # hash dictionary words in lower case
    hash_lower = hashlib.sha256(salted_dictionary_lower).hexdigest()
    hashed_dictionary_lower.append(hash_lower)
    
    # hash dictionary words in upper case
    hash_upper = hashlib.sha256(salted_dictionary_upper).hexdigest()
    hashed_dictionary_upper.append(hash_upper)
    
    # hash dictionary words whth first letter in upper case
    hash_cap = hashlib.sha256(salted_dictionary_capitilized).hexdigest()
    hashed_dictionary_capitilized.append(hash_cap) 

# compare hashed dictionary with hashes
for i in range(1,55):
    # check common passwords
    if hashes[i] in hashed_common:
        print(hashes[i],":", common[hashed_common.index(hashes[i])])
    # check dictionary passwords in lower case
    elif hashes[i] in hashed_dictionary_lower:
        print(hashes[i],":", dictionary[hashed_dictionary_lower.index(hashes[i])])
    # check dictionary passwords in upper case
    elif hashes[i] in hashed_dictionary_upper:
        print(hashes[i],":", dictionary_upper[hashed_dictionary_upper.index(hashes[i])])
    elif hashes[i] in hashed_dictionary_capitilized:
        print(hashes[i],":", dictionary_cap[hashed_dictionary_capitilized.index(hashes[i])])
    #elif hashes[i] in hashed_common_numbers_special:
        #print(hashes[i],":", common_numbers_special[hashed_common_numbers_special.index(hashes[i])])
    else:
        print(hashes[i],":", "")






