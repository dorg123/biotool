import typing
from functools import reduce

from biogate.seq.dna import DNA
from biogate.seq.rna import RNA


def reverse_transcript(rna: RNA) -> DNA:
    return DNA(rna.replace('U', 'T').data)


def parametrize(options: typing.Sequence[typing.Sequence]) -> typing.Sequence:
    maximum = [len(option) for option in options]
    maximum_options = reduce(lambda current, item: current * item, maximum)
    counter = [0] * len(options)
    output_sequences = []

    def increment_counter():
        counter[0] += 1
        for i in range(len(options)):
            if counter[i] < maximum[i]:
                break
            counter[i] = 0
            counter[i + 1] += 1

    for _ in range(maximum_options):
        output_sequences.append([options[i] for i in counter])
        increment_counter()

    return output_sequences
