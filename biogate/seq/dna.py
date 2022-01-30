from biogate.seq.bioseq import BioSequence
from biogate.seq.rna import RNA


class DNA(BioSequence):
    nucleotides = frozenset('ATGC')
    allowed_characters = frozenset('ATGCRYSWKMBDHVN.')
    placeholders = {'W': {'A', 'T'}, 'M': {'A', 'C'}, 'K': {'G', 'T'}, 'R': {'A', 'G'}, 'Y': {'C', 'T'},
                    'B': {'C', 'G', 'T'}, 'D': {'A', 'G', 'T'}, 'H': {'A', 'C', 'T'}, 'V': {'A', 'C', 'G'},
                    'N': nucleotides, 'S': {'G', 'C'}}
    complementary_letters = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'R': 'Y', 'Y': 'R', 'K': 'M', 'M': 'K', 'B': 'V',
                             'V': 'B', 'D': 'H', 'H': 'D'}

    def __repr__(self):
        return f'dna{repr(self.data)}'

    @property
    def complementary(self):
        return DNA(''.join(self.complementary_letters.get(letter, letter) for letter in self.data))

    def transcript(self) -> RNA:
        return RNA(self.data.replace('T', 'U'))

