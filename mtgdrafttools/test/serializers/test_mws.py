import unittest

from mtgdrafttools.expansions.utils import get_expansion
from mtgdrafttools.serializers.mws import MWSSerializer


class TestMWSSerializer(unittest.TestCase):

    def test_generic_serializer_serialize_pack_success(self):
        """
        Tests that a pack can successfully be serialized.
        """
        # generate a pack
        expansion = get_expansion('dgm')
        pack = expansion.generate_pack()

        cards_to_serialize = pack.cards + pack.cards
        serializer = MWSSerializer()
        #import ipdb; ipdb.set_trace();
        serialized_cards = serializer.serialize(cards_to_serialize)
        #import ipdb; ipdb.set_trace();
        # go through each card that was supposed to be serialized and
        for card in cards_to_serialize:
            self.assertTrue(card.name in serialized_cards)
