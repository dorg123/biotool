"""
Name        dna.py
Purpose     A class that represents a DNA sequence
Author      Dor Genosar (dor.genosar@outlook.com)
Change log
    2019 03 16  Created
"""

from biogate.seq.bioseq import BioSequence
from biogate.seq.rna import RNA


class DNA(BioSequence):
    letters = frozenset('ATGCRYSWKMBDHVN.-')
    wildcards = {'R': {'A', 'G'}, 'Y': {'C', 'T'}, 'S': {'G', 'C'}, 'W': {'A', 'T'}, 'K': {'G', 'T'}, 'M': {'A', 'C'},
                 'B': {'C', 'G', 'T'}, 'D': {'A', 'G', 'T'}, 'H': {'A', 'C', 'G'}, 'V': {'A', 'C', 'G'},
                 'N': {'A', 'T', 'G', 'C'}}
    complementary_letters = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'R': 'Y', 'Y': 'R', 'K': 'M', 'M': 'K', 'B': 'V',
                             'V': 'B', 'D': 'H', 'H': 'D'}

    def __init__(self, sequence: str):
        super().__init__(sequence.upper())

    @property
    def complementary(self):
        return DNA(''.join(map(lambda x: self.complementary_letters.get(x, x), self.data)))

    def transcript(self):
        return RNA(self.data.replace('T', 'U'))

