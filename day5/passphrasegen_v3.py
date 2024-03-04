# https://xkcd.com/936/

import random

def read_wordlist(filename):
  with open(filename, "r") as file:
    words = file.read().splitlines()
  return words

def generate_passphrase(wordlist, length=5, separator=" "):
  chosen_words = random.sample(wordlist, length)
  return separator.join(chosen_words)


wordlist = read_wordlist("combined.txt")
passphrase = generate_passphrase(wordlist)
passphrase2 = generate_passphrase(wordlist)
passphrase3 = generate_passphrase(wordlist)
passphrase4 = generate_passphrase(wordlist)
passphrase5 = generate_passphrase(wordlist)

print('''
 ad8888888888ba
dP'         `"8b,
8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
8  8' `8           "8baaaad""""baaaad""""baad""8b
8  8   8              """"      """"      ""    8b
8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
8  `"""'       ,d8""
Yb,         ,ad8"    
 "Y8888888888P"
''')
print("Welcome to the Random Passphrase Generator")
print("-----------------------------------------------")

print("Generated Passphrases: ")
print(" ")
print("1)", passphrase)
print("2)", passphrase2)
print("3)" , passphrase3)
print("4)", passphrase4)
print("5)", passphrase5)