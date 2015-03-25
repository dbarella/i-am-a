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
      'kitten-sitting',
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
      'cat',
      'diamond',
      'dog',
      'dollhouse',
      'grapefruit',
      'kitten',
      'muncher',
      'octopus',
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
