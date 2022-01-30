import typing


class Record(object):
    def __init__(self, source: str, record_type: str, identifier: str, **properties: typing.Dict[str, typing.Any]):
        self.__dict__.update(properties)
        self.__properties = properties
        self.__record_type = record_type
        self.__id = identifier
        self.__source = source

    @property
    def source(self):
        return self.__source

    @property
    def record_type(self):
        return self.__record_type

    @property
    def identifier(self):
        return self.__id

    @property
    def extra(self):
        return self.__properties

    def __repr__(self):
        return f'<{self.__source} Record [{self.__record_type}] #{self.__id} +{len(self.__properties)} extra>'
