"""
Name        peptide.py
Purpose     A class that represents a Peptide sequence
Author      Dor Genosar (dor.genosar@outlook.com)
Change log
    2019 03 16  Created
"""

from biogate.seq.bioseq import BioSequence


class Peptide(BioSequence):
    letters = frozenset('ACDEFGHIJKLMNPQRSTVWY')
    names = {'A': 'Alanine', 'C': 'Cysteine', 'D': 'Aspartic Acid', 'E': 'Glutamic Acid', 'F': 'Phenylalanine',
             'G': 'Glycine', 'H': 'Histidine', 'I': 'Isoleucine', 'K': 'Lysine', 'L': 'Leucine', 'M': 'Methionine',
             'N': 'Asparagine', 'P': 'Proline', 'Q': 'Glutamine', 'R': 'Arginine', 'S': 'Serine', 'T': 'Threonine',
             'V': 'Valine', 'W': 'Tryptophan', 'Y': 'Tyrosine'}
    codes = {'A': 'Ala', 'C': 'Cys', 'D': 'Asp', 'E': 'Glu', 'F': 'Phe', 'G': 'Gly', 'H': 'His', 'I': 'Ile', 'K': 'Lys',
             'L': 'Leu', 'M': 'Met', 'N': 'Asn', 'P': 'Pro', 'Q': 'Gln', 'R': 'Arg', 'S': 'Ser', 'T': 'Thr', 'V': 'Val',
             'W': 'Trp', 'Y': 'Tyr'}
    codons = \
        {'M': {'AUG'}, 'W': {'UGG'}, 'C': {'UGU', 'UGC'}, 'D': {'GAU', 'GAC'}, 'E': {'GAA', 'GAG'}, 'F': {'UUU', 'UUC'},
         'H': {'CAU', 'CAC'}, 'K': {'AAA', 'AAG'}, 'N': {'AAU', 'AAC'}, 'Q': {'CAA', 'CAG'}, 'Y': {'UAU', 'UAC'},
         '*': {'UAA', 'UGA', 'UAG'}, 'I': {'AUU', 'AUC', 'AUA'}, 'A': {'GCU', 'GCC', 'GCA', 'GCG'},
         'G': {'GGU', 'GGC', 'GGA', 'GGG'}, 'P': {'CCU', 'CCC', 'CCA', 'CCG'}, 'T': {'ACU', 'ACC', 'ACA', 'ACG'},
         'V': {'GUU', 'GUC', 'GUA', 'GUG'}, 'L': {'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'},
         'R': {'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'}, 'S': {'UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'}}

    def __init__(self, sequence: str):
        super().__init__(sequence.upper())


Protein = Peptide
