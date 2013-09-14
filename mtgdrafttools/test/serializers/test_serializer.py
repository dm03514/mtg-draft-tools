import os
import unittest

from mtgdrafttools import serializers 
from mtgdrafttools import settings
from mtgdrafttools.expansions.expansions import Expansion
from mtgdrafttools.expansions.utils import get_expansion

class TestSerializer(unittest.TestCase):

    def test_serializers_serializer_mws(self):
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


class TestDeserializer(unittest.TestCase):
    
    def test_serializers_deserializer_mws(self):
        """
        Tests that deserialze method returns an expansion object, when given a vaild file.
        """
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 
                                                   settings.SUPPORTED_EXPANSIONS['dgm'])
        expansion = serializers.deserialize('mws', expansion_txt_file_location) 
        self.assertIsInstance(expansion, Expansion)
        
