"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    '''Function that finds random words from a dictionary

    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    ' porcupine'

    >>> wf.random()
    'dog

    '''

    def __init__(self, path):
        file = open(path)
        self.words = self.parse(file)
        print(f'{len(self.words)} words read')

    def parse(self, file):
        '''Parse dictionary into list of words and remove any spaces at the beginning or at the end'''
        return [line.strip() for line in file]

    def random(self):
        '''Returns a random word'''
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    '''Extended WordFinder that excludes hashtags or spaces

     >>> swf = SpecialWordFinder("complex.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    '''

    def parse(self, file):
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]
