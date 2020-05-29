"""
Name        reader.py
Purpose     An abstract class for a file reader
Author
Dor Genosar (dor.genosar@outlook.com)
Change log
    2019 03 16  Created
"""

import abc


class FileReader(object, metaclass=abc.ABCMeta):
    """
    A base class for different format file readers
    """

    def __init__(self, filename):
        """
        Initialize a new file reader
        :param filename: A path to a
        """

        self.__filename = filename

    @property
    def filename(self):
        return self.__filename
