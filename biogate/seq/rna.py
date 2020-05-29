"""
Name        rna.py
Purpose     A class that represents an RNA sequence
Author      Dor Genosar (dor.genosar@outlook.com)
Change log
    2019 03 16  Created
"""

from biogate.seq.bioseq import BioSequence
from biogate.seq.peptide import Peptide
import re


class RNA(BioSequence):
    letters = frozenset('AUGCRYSWKMBDHVN.-')
    wildcards = {'R': {'A', 'G'}, 'Y': {'C', 'U'}, 'S': {'G', 'C'}, 'W': {'A', 'U'}, 'K': {'G', 'U'}, 'M': {'A', 'C'},
                 'B': {'C', 'G', 'U'}, 'D': {'A', 'G', 'U'}, 'H': {'A', 'C', 'G'}, 'V': {'A', 'C', 'G'},
                 'N': {'A', 'U', 'G', 'C'}}
    complementary_letters = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G', 'R': 'Y', 'Y': 'R', 'K': 'M', 'M': 'K', 'B': 'V',
                             'V': 'B', 'D': 'H', 'H': 'D'}
    codon_length = 3
    start_codon = 'AUG'
    end_codons = {'UAA', 'UGA', 'UAG'}
    codons = \
        {'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C', 'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',
         'UUA': 'L', 'UCA': 'S', 'UAA': '*', 'UGA': '*', 'UUG': 'L', 'UCG': 'S', 'UAG': '*', 'UGG': 'W',
         'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R', 'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
         'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
         'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S', 'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
         'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', 'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
         'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G', 'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
         'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', 'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}
    translating_re = re.compile(r'(AUG)(\w{3})*(UAA|UGA|UAG)')

    def __init__(self, sequence: str):
        super().__init__(sequence.upper())

    @property
    def complementary(self):
        return RNA(''.join(map(lambda x: self.complementary_letters.get(x, x), self.data)))

    def translate_whole(self):
        return Peptide(''.join(RNA.codons.get(codon, '') for codon in self.chunk(RNA.codon_length)))

    def translate(self):
        sequence = RNA.translating_re.search(self.data)
        if not sequence:
            raise ValueError('Sequence start/stop codons could not be found.')
        return RNA(sequence.group()).translate_whole()
