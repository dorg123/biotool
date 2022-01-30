import abc
import collections
import typing


class SequenceMeta(abc.ABCMeta):
    def __or__(cls, other: str):
        return cls(other)


class BioSequence(collections.UserString, metaclass=SequenceMeta):
    allowed_characters = frozenset()

    def __init__(self, sequence: str):
        sequence = sequence.upper()
        if set(sequence) <= self.allowed_characters:
            super().__init__(sequence)
        else:
            raise ValueError(f"The sequence contains chars other than [{''.join(sorted(self.allowed_characters))}]")

    def chunk(self, length: int) -> typing.Iterable[typing.AnyStr]:
        return [self[i:i + length] for i in range(0, len(self), length)]
