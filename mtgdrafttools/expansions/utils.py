import os

from mtgdrafttools import settings
from mtgdrafttools.expansionparser import parse_expansion_file


def get_expansion(abbrev):
    """
    Returns an `Expansion` instance for the corresponding abbrev.
    Loads/parses expansions file.
    @param abbrev string one of the supported expansions
    """
    expansion_txt_file_location = os.path.join(settings.DATA_DIR, 
                                               settings.SUPPORTED_EXPANSIONS[abbrev])
    return parse_expansion_file(expansion_txt_file_location)
