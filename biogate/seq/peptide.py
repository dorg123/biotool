import typing
from string import ascii_uppercase

from biogate.seq.bioseq import BioSequence


class Peptide(BioSequence):
    amino_acids = frozenset('ACDEFGHIKLMNOPQRSTUVWY')
    allowed_characters = frozenset(ascii_uppercase + '+-ΦΩΨπζ.')
    placeholders = {'X': amino_acids, 'B': {'D', 'N'}, 'Z': {'E', 'Q'}, 'J': {'I', 'L'}, '-': {'D', 'E'},
                    'Φ': {'V', 'I', 'L', 'F', 'W', 'Y', 'M'}, 'Ψ': {'V', 'I', 'L', 'M'}, 'Ω': {'F', 'W', 'Y', 'H'},
                    'π': {'P', 'G', 'A', 'S'}, 'ζ': {'S', 'T', 'H', 'N', 'Q', 'E', 'D', 'K', 'R'}, '+': {'K', 'R', 'H'}}
    names = {'A': 'Alanine', 'C': 'Cysteine', 'D': 'Aspartic Acid', 'E': 'Glutamic Acid', 'F': 'Phenylalanine',
             'G': 'Glycine', 'H': 'Histidine', 'I': 'Isoleucine', 'K': 'Lysine', 'L': 'Leucine', 'M': 'Methionine',
             'N': 'Asparagine', 'O': 'Pyrrolysine', 'P': 'Proline', 'Q': 'Glutamine', 'R': 'Arginine', 'S': 'Serine',
             'T': 'Threonine', 'U': 'Selenocysteine', 'V': 'Valine', 'W': 'Tryptophan', 'Y': 'Tyrosine'}
    codes = {'A': 'Ala', 'C': 'Cys', 'D': 'Asp', 'E': 'Glu', 'F': 'Phe', 'G': 'Gly', 'H': 'His', 'I': 'Ile', 'K': 'Lys',
             'L': 'Leu', 'M': 'Met', 'N': 'Asn', 'P': 'Pro', 'Q': 'Gln', 'R': 'Arg', 'S': 'Ser', 'T': 'Thr', 'V': 'Val',
             'W': 'Trp', 'Y': 'Tyr', 'U': 'Sec', 'O': 'Pyl', 'X': 'Xaa', 'B': 'Asx', 'Z': 'Glx', 'J': 'Xle'}
    codons = {'C': {'UGU', 'UGC'}, 'F': {'UUU', 'UUC'}, 'M': {'AUG'}, 'W': {'UGG'}, 'O': {'UAG'}, 'U': {'UGA'},
              'A': {'GCU', 'GCC', 'GCA', 'GCG'}, '*': {'UAA', 'UGA', 'UAG'}, 'Y': {'UAU', 'UAC'}, 'H': {'CAU', 'CAC'},
              'G': {'GGU', 'GGC', 'GGA', 'GGG'}, 'I': {'AUU', 'AUC', 'AUA'}, 'E': {'GAA', 'GAG'}, 'K': {'AAA', 'AAG'},
              'L': {'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'}, 'V': {'GUU', 'GUC', 'GUA', 'GUG'}, 'Q': {'CAA', 'CAG'},
              'R': {'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'}, 'T': {'ACU', 'ACC', 'ACA', 'ACG'}, 'N': {'AAU', 'AAC'},
              'S': {'UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'}, 'P': {'CCU', 'CCC', 'CCA', 'CCG'}, 'D': {'GAU', 'GAC'}}
    placeholder_codons = {'A': {'GCN'}, 'N': {'AAY'}, 'D': {'GAY'}, 'C': {'UGY'}, 'Q': {'CAR'}, 'R': {'MGR', 'CGY'},
                          'G': {'GGN'}, 'H': {'CAY'}, 'I': {'AUH'}, 'K': {'AAR'}, 'F': {'UUY'}, 'Ψ': {'VUN', 'UUR'},
                          'T': {'ACN'}, 'Y': {'UAY'}, 'V': {'GUN'}, 'X': {'NNN'}, 'B': {'RAY'}, 'L': {'YUR', 'CUY'},
                          '-': {'GAN'}, 'O': {'UAG'}, 'U': {'UGA'}, 'E': {'GAR'}, 'P': {'CCN'}, 'S': {'UCN', 'AGY'},
                          'J': {'YUR', 'AUH', 'CUY'}, 'Φ': {'NUN', 'UAY', 'UGG'}, 'M': {'AUG'},
                          'Ω': {'YWY', 'UUY', 'UGG'}, 'π': {'BCN', 'RGY', 'GGR'}, 'Z': {'SAR'},
                          'ζ': {'VAN', 'WCN', 'CGN', 'AGY'}, '+': {'ARR', 'CRY', 'CGR'}, 'W': {'UGG'}}

    @classmethod
    def resolve_codons_for_amino_acid(cls, amino_acid) -> typing.Sequence[str]:
        if amino_acid in cls.codons:
            return list(cls.codons[amino_acid])
        elif amino_acid in cls.placeholders:
            return sum((cls.resolve_codons_for_amino_acid(aa) for aa in cls.placeholders[amino_acid]), [])
        else:
            raise ValueError(f'{amino_acid} is not a known amino acid or placeholder')

    def __repr__(self):
        return f'p{repr(self.data)}'

    def resolve_codons(self) -> typing.Sequence[typing.Sequence]:
        return [self.resolve_codons_for_amino_acid(aa) for aa in self.data]

    def resolve_codons_with_placeholders(self) -> typing.Sequence[typing.Sequence]:
        return [list(self.placeholder_codons[aa]) for aa in self.data]

    def possible_rna_count(self) -> int:
        pass


Protein = Peptide
