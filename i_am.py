#!/usr/bin/env python
"""I am a(n) adjective noun."""


import random
import sys


VOWELS = ('a', 'e', 'i', 'o', 'u')


ADJECTIVES = [
    'alphabetical',
    'apple-eyed',
    'carbon-based',
    'cheery-eyed',
    'couch-like',
    'earl-grey',
    'flubbery',
    'half-silvered',
    'inconvenient',
    'kitten-sitting',
    'kitten-sniffing',
    'large',
    'lexicographic',
    'medium-large',
    'medium-sized',
    'poorly-organized',
    'small',
    'soury-eyed',
    'yammering',
    'yttrium-based',
    ]


NOUNS = [
    'aviary',
    'bar of chocolate',
    'blade of grass',
    'cat',
    'ceiling fan',
    'chocolate-eater',
    'couch-sitter',
    'dog',
    'dogster',
    'dollhouse',
    'fridge-opener',
    'grapefruit',
    'hash collision',
    'kitten',
    'kitten-sitter',
    'kitten-stealer',
    'kitten-thief',
    'muncher',
    'octopus',
    'octothorpe',
    'pupster',
    'rabble-rouser',
    'ruffian',
    'smolderer',
    'street-walker',
    'sub-woofer',
    'syrup',
    'tail-dragger',
    'thief',
    'woofer',
    ]


def a():
  adjective = random.choice(ADJECTIVES)
  noun = random.choice(NOUNS)

  if adjective.startswith(VOWELS):
    article = 'an'
  else:
    article = 'a'

  # I am a(n) adjective noun.
  return 'I am {0} {1} {2}.'.format(article, adjective, noun)


def main():
  i_am_a = a  # Functor for cuteness

  # I am a(n)... multiple times
  if len(sys.argv) == 2 and sys.argv[1].isdigit():
    for _ in range(int(sys.argv[1])):
      print i_am_a()

  else:  # Otherwise just a single run
    # I am a(n)...
    print i_am_a()


if __name__ == '__main__':
  main()
