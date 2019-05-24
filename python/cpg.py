#!/usr/bin/python   
import random
from random import randint

r = random.SystemRandom()

# Out list of words to use
with open('../lists/mixed.txt') as f:
    words = [w.strip() for w in f]

def generate_password(words, k, numbers=None, characters=None,
                      first_upper=True, ins=True):
    """Return a random password based on a sorted word list."""
    elements = r.sample(words, k)
    if numbers:
        elements.insert(r.randint(1, len(elements)), r.choice(numbers))
        elements.insert(r.randint(1, len(elements)), r.choice(numbers))
        elements.insert(r.randint(1, len(elements)), r.choice(numbers))
    if characters:
        elements.insert(r.randint(1, len(elements)), r.choice(characters))
        elements.insert(r.randint(1, len(elements)), r.choice(characters))
    if first_upper:
        elements[0] = elements[0].title()

    return ''.join(elements)

splitters = [
    '@',
    '^',
    '&',
    '*',
    '_',
    '~',
    '?',
    '=',
    '+',
    '-'
]

gen_without_split = generate_password(words, 3, numbers='0123456789', characters='~#$%^&*\[]{}"<>,.?/')
password = list(gen_without_split)
split = password.insert(r.randint(1, len(password)), r.choice(splitters))
s = ''
print (s.join(password))
