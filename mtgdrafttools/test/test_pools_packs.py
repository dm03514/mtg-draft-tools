import os
import unittest

from expansionparser import parse_expansion_file, sort_by_rarity
from pools.packs import generate_pack

class TestPoolsPacks(unittest.TestCase):

    def test_generate_pack_for_dgm(self):
        """
        Test that a dragons maze pack can be generated successfully.
        """
        script_location = os.path.abspath(os.path.dirname(__file__))
        expansion_txt_file_location = os.path.join(script_location, '..', '..', 'expansions', 'DGM.txt')
        cards_list = parse_expansion_file(expansion_txt_file_location)
        cards_by_rarity = sort_by_rarity(cards_list)
        pack = generate_pack(cards_by_rarity)
        self.assertEqual(len(pack.cards), 14)
        self.assertEqual(len(pack.commons), 10)
        self.assertEqual(len(pack.uncommons), 3)
        self.assertEqual(len(pack.rares), 1)
        #import ipdb; ipdb.set_trace();
