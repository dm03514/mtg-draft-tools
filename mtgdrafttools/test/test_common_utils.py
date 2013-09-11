import os
import unittest

from common.utils import parse_expansion_file


class TestCommonUtils(unittest.TestCase):

    def test_parse_expansion_file_into_cards(self):
        """
        Tests that given an expansion text file in the MWS format we 
        can get a set of cards from it.
        """
        script_location = os.path.abspath(os.path.dirname(__file__))
        expansion_txt_file_location = os.path.join(script_location, '..', '..', 'expansions', 'DGM.txt')
        #import pdb; pdb.set_trace();
        cards_set = parse_expansion_file(expansion_txt_file_location)
