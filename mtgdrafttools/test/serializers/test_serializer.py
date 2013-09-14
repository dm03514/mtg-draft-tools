import unittest

from mtgdrafttools import serializers 
from mtgdrafttools.expansions.utils import get_expansion

class TestSerializer(unittest.TestCase):

    def test_serializer_serializer_mws(self):
        """
        Tests that we can succuessfully serializer cards in mws format.
        """
        expansion = get_expansion('dgm')
        pack = expansion.generate_pack()
        cards_to_serialize = pack.cards + pack.cards
        #import ipdb; ipdb.set_trace();
        serialized_cards = serializers.serialize('mws', cards_to_serialize)
        for card in cards_to_serialize:
            self.assertTrue(card.name in serialized_cards)
