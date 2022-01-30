import re

from biogate.seq.bioseq import BioSequence
from biogate.seq.peptide import Peptide


class RNA(BioSequence):
    nucleotides = frozenset('AUGC')
    allowed_characters = frozenset('AUGCRYSWKMBDHVN.')
    placeholders = {'W': {'A', 'U'}, 'M': {'A', 'C'}, 'K': {'G', 'U'}, 'R': {'A', 'G'}, 'Y': {'C', 'U'},
                    'B': {'C', 'G', 'U'}, 'D': {'A', 'G', 'U'}, 'H': {'A', 'C', 'U'}, 'V': {'A', 'C', 'G'},
                    'N': nucleotides, 'S': {'G', 'C'}}
    complementary_letters = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G', 'R': 'Y', 'Y': 'R',
                             'K': 'M', 'M': 'K', 'B': 'V', 'V': 'B', 'D': 'H', 'H': 'D'}
    codon_length = 3
    start_codon = 'AUG'
    end_codons = {'UAA', 'UGA', 'UAG'}
    codons = {'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C', 'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',
              'UUA': 'L', 'UCA': 'S', 'UAA': '*', 'UGA': '*', 'UUG': 'L', 'UCG': 'S', 'UAG': '*', 'UGG': 'W',
              'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R', 'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
              'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
              'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S', 'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
              'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', 'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
              'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G', 'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
              'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', 'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G',
              # placeholders
              'GCN': 'A', 'AAY': 'N', 'GAY': 'D', 'UGY': 'C', 'CAR': 'Q', 'GAR': 'E', 'GGN': 'G', 'CAY': 'H',
              'AUH': 'I', 'AAR': 'K', 'UUY': 'F', 'CCN': 'P', 'ACN': 'T', 'UAY': 'Y', 'GUN': 'V', 'NNN': 'X',
              'RAY': 'B', 'SAR': 'Z', 'GAN': '-'}
    translation_regex = re.compile(r'(AUG([AUGCRYSWKMBDHVN]{3})*)(UAA|UGA|UAG|UAR)')

    def __repr__(self):
        return f'rna{repr(self.data)}'

    @property
    def complementary(self):
        return RNA(''.join(self.complementary_letters.get(letter, letter) for letter in self.data))

    def translate_whole(self) -> Peptide:
        """
        Translate the RNA sequence as a whole
        :return: A matching peptide
        """
        return Peptide(''.join(self.codons.get(codon, '.') for codon in self.chunk(self.codon_length)))

    def translate(self) -> Peptide:
        """
        Translate the RNA sequence with start and end codons
        :return: A matching peptide
        """
        sequence = self.translation_regex.search(self.data)
        if not sequence:
            raise ValueError('Sequence start/stop codons could not be found.')
        return RNA(sequence.group(1)).translate_whole()
