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
    salted_word = (salt + imput).encode('utf-8')
    hash_value = hashlib.sha256(salted_word).hexdigest()
    hashed_common.append(hash_value)

# common passwords with numbers and special characters
common_numbers_special = []
hashed_common_numbers_special = []
list_of_numbers_symbols = ['0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',';',':','<','>','?','/']
for i in range(1,1000):
    for j in range(len(list_of_numbers_symbols)):
      for k in range(len(list_of_numbers_symbols)):
        for l in range(len(list_of_numbers_symbols)):
          common_numbers_special.append(common[i] + list_of_numbers_symbols[j] + list_of_numbers_symbols[k])
          salted_common_numbers_special = (salt + common[i] + list_of_numbers_symbols[j] + list_of_numbers_symbols[k]).encode('utf-8')
          hash_common_numbers_special = hashlib.sha256(salted_common_numbers_special).hexdigest()
          hashed_common_numbers_special.append(hash_common_numbers_special)


# # dictionary pawwords
# dictionary = []
# with open("/Users/davidjiang/Info_sec/lab3/dictionary_58110.txt", "r") as f:
#   for line in f:
#     imput = line.strip()
#     dictionary.append(imput)

# # concatinate common passwords and dictionary words
# commonAndDictionn_dictionary = []
# commonAndDictionn_dictionary_hashed = []
# for i in range(1,1000):
#     for j in range(len(dictionary)):
#         commonAndDictionn_dictionary.append(common[i] + dictionary[j])
#         hash= hashlib.sha256((salt + common[i] + dictionary[j]).encode('utf-8')).hexdigest()
#         commonAndDictionn_dictionary_hashed.append(hash)

# # concatinate common passwords and common passwords
# commonAndCommon_dictionary = []
# commonAndCommon_dictionary_hashed = []
# for i in range(1,1000):
#     for j in range(len(common)):
#         commonAndCommon_dictionary.append(common[i] + common[j])
#         hash= hashlib.sha256((salt + common[i] + common[j]).encode('utf-8')).hexdigest()
#         commonAndCommon_dictionary_hashed.append(hash)

# # concatinate dictionary words and dictionary words
# dictionaryAndDictionary_dictionary = []
# dictionaryAndDictionary_dictionary_hashed = []
# for i in range(58110):
#     for j in range(len(dictionary)):
#         dictionaryAndDictionary_dictionary.append(dictionary[i] + dictionary[j])
#         hash= hashlib.sha256((salt + dictionary[i] + dictionary[j]).encode('utf-8')).hexdigest()
#         dictionaryAndDictionary_dictionary_hashed.append(hash)

# for i in range(1,55):
    # check common passwords
    if hashes[i] in hashed_common:
        print(hashes[i],":", common[hashed_common.index(hashes[i])])
    # elif hashes[i] in hashed_common_numbers_special:
    #     print(hashes[i],":", common_numbers_special[hashed_common_numbers_special.index(hashes[i])])
    # check dictionary passwords in lower case
    # elif hashes[i] in commonAndDictionn_dictionary_hashed:
    #     print(hashes[i],":", commonAndDictionn_dictionary[commonAndDictionn_dictionary_hashed.index(hashes[i])])
    # # check dictionary passwords in upper case
    # elif hashes[i] in commonAndCommon_dictionary_hashed:
    #     print(hashes[i],":", commonAndCommon_dictionary[commonAndCommon_dictionary_hashed.index(hashes[i])])
    # elif hashes[i] in dictionaryAndDictionary_dictionary_hashed:
    #     print(hashes[i],":", dictionaryAndDictionary_dictionary[dictionaryAndDictionary_dictionary_hashed.index(hashes[i])])
    else:
        print(hashes[i],":", "")






  


