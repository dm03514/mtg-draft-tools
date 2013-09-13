import os
import unittest

from mtgdrafttools.expansionparser import parse_expansion_file, sort_by_rarity
from mtgdrafttools.pools.packs import generate_pack
from mtgdrafttools.serializers.generic import GenericSerializer


class TestGenericSerializer(unittest.TestCase):

    def test_generic_serializer_serialize_pack_success(self):
        """
        Tests that a pack can successfully be serialized.
        """
        # generate a pack
        script_location = os.path.abspath(os.path.dirname(__file__))
        expansion_txt_file_location = os.path.join(script_location, '..', '..', 'expansions', 'DGM.txt')
        cards_list = parse_expansion_file(expansion_txt_file_location)
        cards_by_rarity = sort_by_rarity(cards_list)
        pack = generate_pack(cards_by_rarity)
        #import ipdb; ipdb.set_trace();
