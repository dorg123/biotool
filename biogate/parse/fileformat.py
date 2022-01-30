import abc
import typing
from typing import IO


class FileFormat(object, metaclass=abc.ABCMeta):
    def __init__(self, file: IO):
        self.__file = file

    @abc.abstractmethod
    def read(self) -> typing.Generator:
        pass

    @abc.abstractmethod
    def write_one(self, record):
        pass

    def write_many(self, records: typing.Iterable):
        for record in records:
            self.write_one(record)
