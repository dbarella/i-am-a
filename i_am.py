#!/usr/bin/env python
"""I am a(n) adjective noun."""


import random


VOWELS = ('a', 'e', 'i', 'o', 'u')


def a():
  adjective = random.choice([
      'apple-eyed',
      'carbon-based',
      'cheery-eyed',
      'earl-grey',
      'flubbery',
      'inconvenient',
      'kitten-sitting',
      'kitten-sniffing',
      'large',
      'lexicographic',
      'medium-sized',
      'small',
      'soury-eyed',
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
      'grapefruit',
      'kitten',
      'kitten-sitter',
      'muncher',
      'octopus',
      'pupster',
      'rabble-rouser',
      'smolderer',
      'syrup',
      'tail-dragger',
      ])

  if adjective.startswith(VOWELS):
    article = 'an'
  else:
    article = 'a'

  # I am a(n) adjective noun.
  return 'I am {0} {1} {2}.'.format(article, adjective, noun)


def main():
  # I am a(n)...
  print a()


if __name__ == '__main__':
  main()
