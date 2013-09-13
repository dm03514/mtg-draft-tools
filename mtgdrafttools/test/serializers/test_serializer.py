import os
import unittest

from mtgdrafttools.expansionparser import parse_expansion_file
from mtgdrafttools import serializers 

class TestSerializer(unittest.TestCase):

    def test_serializer_serializer_mws(self):
        """
        Tests that we can succuessfully serializer cards in mws format.
        """
        script_location = os.path.abspath(os.path.dirname(__file__))
        expansion_txt_file_location = os.path.join(script_location, '..', '..', '..', 'data', 'DGM.txt')
        expansion = parse_expansion_file(expansion_txt_file_location)
        pack = expansion.generate_pack()
        cards_to_serialize = pack.cards + pack.cards
        #import ipdb; ipdb.set_trace();
        serialized_cards = serializers.serialize('mws', cards_to_serialize)
        for card in cards_to_serialize:
            self.assertTrue(card.name in serialized_cards)
