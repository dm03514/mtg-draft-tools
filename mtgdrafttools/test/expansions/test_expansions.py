import os
import unittest

from mtgdrafttools import settings
from mtgdrafttools.expansionparser import parse_expansion_file


class TextExpansion(unittest.TestCase):
    
    def test_sort_by_rarity(self):
        """
        Tests that an expansion can be successfully sorted by rarity.
        """
        #import ipdb; ipdb.set_trace();
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 'DGM.txt')
        expansion = parse_expansion_file(expansion_txt_file_location)
        cards_by_rarity = expansion._get_cards_by_rarity()
        for key in ['C', 'U', 'R']:
            self.assertTrue(key in cards_by_rarity)

    def test_generate_pack_for_dgm(self):
        """
        Test that a dragons maze pack can be generated successfully.
        """
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 'DGM.txt')
        expansion = parse_expansion_file(expansion_txt_file_location)
        pack = expansion.generate_pack()
        self.assertEqual(len(pack.cards), 14)
        self.assertEqual(len(pack.commons), 10)
        self.assertEqual(len(pack.uncommons), 3)
        self.assertEqual(len(pack.rares), 1)
