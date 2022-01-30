import abc
import collections
import typing
import pkg_resources
from typing import IO

from pkg_resources import EntryPoint


class FileReader(collections.Iterable, metaclass=abc.ABCMeta):
    """
    A base class for different format file readers
    """

    def __init__(self, filename: typing.AnyStr, file_format: typing.AnyStr):
        """
        Initialize a new file reader
        :param filename: A path to a file with records to read
        """

        formatter_entry_point: EntryPoint = next(pkg_resources.iter_entry_points('biogate.formats', file_format))
        self.__formatter_class = formatter_entry_point.load()
        self.__filename = filename
        self.__format = file_format
        self.__file: 'IO' = None

    def __enter__(self) -> 'FileReader':
        self.__file = open(self.__filename)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__file.close()

    def __iter__(self):
        yield from self.__formatter_class(self.__file).read()

    @property
    def filename(self):
        return self.__filename

    @property
    def file_format(self):
        return self.__format
