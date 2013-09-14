import os

from mtgdrafttools import serializers

def get_expansion(abbrev):
    """
    Returns an `Expansion` instance for the corresponding abbrev.
    Loads/parses expansions file.
    @param abbrev string one of the supported expansions
    """
    return serializers.deserialize('mws', abbrev) 
