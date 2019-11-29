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
  article = indefinite_article_for(adjective)

  # I am a(n) adjective noun.
  return 'I am {0} {1} {2}.'.format(article, adjective, noun)

def indefinite_article_for(word):
  if word.startswith(VOWELS):
    return 'an'
  elif word.startswith('y'):
    # Good old 'sometimes y'...

    if len(word) == 1:
      raise ValueError("'y' is not a word in English, what are you doing?")

    if word[1] in VOWELS:
      # If 'y' is being followed by a vowel, assume it's acting as a consonant (e.g. 'a yellow hat').
      return 'a'
    else:
      # If 'y' is being followed by a consonant, assume it's acting as a vowel (e.g. 'an yttrium-based life-form').
      return 'an'
  else:
    return 'a'

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
