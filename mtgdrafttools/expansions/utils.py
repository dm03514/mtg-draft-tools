import os

from mtgdrafttools import settings
from mtgdrafttools import serializers


def get_expansion(abbrev):
    """
    Returns an `Expansion` instance for the corresponding abbrev.
    Loads/parses expansions file.
    @param abbrev string one of the supported expansions
    """
    expansion_txt_file_location = os.path.join(settings.DATA_DIR, 
                                               settings.SUPPORTED_EXPANSIONS[abbrev])
    return serializers.deserialize('mws', expansion_txt_file_location) 
