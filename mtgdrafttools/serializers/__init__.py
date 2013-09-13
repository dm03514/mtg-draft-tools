"""
Serializers based off of django api:

# https://github.com/django/django/blob/master/django/core/serializers/__init__.py


"""
from .mws import MWSSerializer

_serializers = {
    'mws': MWSSerializer
}


def serialize(serializer_format, cards):
    """
    Serialize a list of cards using a certain serializer.
    @param format string right now only support 'mws'
    """ 
    s = _serializers[serializer_format]()
    s.serialize(cards)
    return s.getvalue()
