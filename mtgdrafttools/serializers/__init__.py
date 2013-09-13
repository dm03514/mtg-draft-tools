"""
Serializers based off of django api:

# https://github.com/django/django/blob/master/django/core/serializers/__init__.py


"""
from .mws import MWSSerializer

_serializers = {
    'mws': MWSSerializer
}
