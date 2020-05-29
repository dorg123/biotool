"""
Name        bioseq.py
Purpose     Base class for bio-sequences of different types
Author      Dor Genosar (dor.genosar@outlook.com)
Change log
    2019 03 20  Created
"""

import collections


class BioSequence(collections.UserString):
    letters = set()

    def __init__(self, sequence: str):
        sequence = sequence.upper()
        if set(sequence) <= self.letters:
            super().__init__(sequence)
        else:
            raise ValueError("'sequence' contains letters other than {}".format(self.letters))

    def chunk(self, length):
        return [self[i:i + length] for i in range(0, len(self), length)]
