#!/usr/bin/env python
"""I am a(n) adjective noun."""


import random
import sys


VOWELS = ('a', 'e', 'i', 'o', 'u')


def a():
  adjective = random.choice([
      'alphabetical',
      'apple-eyed',
      'carbon-based',
      'cheery-eyed',
      'couch-like',
      'earl-grey',
      'flubbery',
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
      ])

  noun = random.choice([
      'aviary',
      'bar of chocolate',
      'blade of grass',
      'cat',
      'chocolate-eater',
      'couch-sitter',
      'dog',
      'dollhouse',
      'fridge-opener',
      'grapefruit',
      'kitten',
      'kitten-sitter',
      'kitten-stealer',
      'kitten-thief',
      'muncher',
      'octopus',
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
      ])

  if adjective.startswith(VOWELS):
    article = 'an'
  else:
    article = 'a'

  # I am a(n) adjective noun.
  return 'I am {0} {1} {2}.'.format(article, adjective, noun)


def main():
  # I am a(n)... multiple times
  if len(sys.argv) == 2 and sys.argv[1].isdigit():
    for _ in range(int(sys.argv[1])):
      print a()

  else:
    # I am a(n)...
    print a()


if __name__ == '__main__':
  main()
