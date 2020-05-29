"""
Name        resolve.py
Purpose     A helper module with resolving functions in the reverse direction from the main dogma
Author      Dor Genosar (dor.genosar@outlook.com)
Change log
    2019 03 24  Created
"""

from biogate.seq.peptide import Peptide
from biogate.seq.rna import RNA
from biogate.seq.dna import DNA
from typing import Sequence


def reverse_transcript(rna: RNA) -> DNA:
    return DNA(rna.replace('U', 'T').data)


def resolve_codons(peptide: Peptide) -> Sequence[RNA]:
    options = [Peptide.codons[aa] for aa in peptide]

