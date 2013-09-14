"""
Serializers based off of django api:

# https://github.com/django/django/blob/master/django/core/serializers/__init__.py


"""
from .mws import MWSSerializer, MWSExpansionDeserializer

_serializers = {
    'mws': MWSSerializer
}

_deserializers = {
    'mws': MWSExpansionDeserializer
}


def serialize(serializer_format, cards):
    """
    Serialize a list of cards using a certain serializer.
    @param format string right now only support 'mws'
    """ 
    s = _serializers[serializer_format]()
    s.serialize(cards)
    return s.getvalue()


def deserialize(deserializer_format, expansion_abbrev):
    """
    Deserialize a file into an `Expansion`
    @param deserializer_format string 
    @param expansion_abbrev string
    """
    d = _deserializers[deserializer_format](expansion_abbrev)
    return d.get_expansion()

