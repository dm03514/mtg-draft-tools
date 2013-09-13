import os
import unittest

from mtgdrafttools import settings
from mtgdrafttools.expansionparser import parse_expansion_file
from mtgdrafttools.serializers.generic import GenericSerializer


class TestGenericSerializer(unittest.TestCase):

    def test_generic_serializer_serialize_pack_success(self):
        """
        Tests that a pack can successfully be serialized.
        """
        # generate a pack
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 'DGM.txt')
        expansion = parse_expansion_file(expansion_txt_file_location)
        pack = expansion.generate_pack()
        cards_to_serialize = pack.cards + pack.cards
        serializer = GenericSerializer()
        serialized_cards = serializer.serialize(cards_to_serialize)
        #import ipdb; ipdb.set_trace();
        # go through each card that was supposed to be serialized and
        for card in cards_to_serialize:
            self.assertTrue(card.name in serialized_cards)
