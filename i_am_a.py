"""I am a(n) adjective noun."""


import random


VOWELS = {'a', 'e', 'i', 'o', 'u'}


def main():
  adjective = random.choice([
      'carbon-based',
      'cheery-eyed',
      'flubbery',
      'kitten-sitting',
      'large',
      'medium-sized',
      'small',
      'soury-eyed',
      'yttrium-biased',
      ])

  noun = random.choice([
      'aviary',
      'cat',
      'dog',
      'dollhouse',
      'kitten',
      'muncher',
      'syrup',
      'tail-dragger',
      'yodeler',
      'grapefruit',
      ])

  if adjective[0] in VOWELS:  # If the first letter of the adj. is a vowel, 'an'
    article = 'an'
  else:
    article = 'a'

  # I am a(n) adjective noun.
  print 'I am {0} {1} {2}.'.format(article, adjective, noun)


if __name__ == '__main__':
  main()
