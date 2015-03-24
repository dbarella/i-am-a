"""I am a(n) adjective noun."""


import random


VOWELS = {'a', 'e', 'i', 'o', 'u'}


def main():
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
      'yttrium-biased',
      ])

  noun = random.choice([
      'aviary',
      'cat',
      'dog',
      'dollhouse',
      'grapefruit',
      'kitten',
      'muncher',
      'syrup',
      'tail-dragger',
      'yodeler',
      ])

  if adjective[0] in VOWELS:  # If the first letter of the adj. is a vowel, 'an'
    article = 'an'
  else:
    article = 'a'

  # I am a(n) adjective noun.
  print 'I am {0} {1} {2}.'.format(article, adjective, noun)


if __name__ == '__main__':
  main()
