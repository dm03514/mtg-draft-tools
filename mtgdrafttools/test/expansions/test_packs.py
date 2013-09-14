import os
import unittest

from mtgdrafttools import settings
from mtgdrafttools.expansionparser import parse_expansion_file

class TextPacks(unittest.TestCase):
   
    def test_pack_filter_by_rarity(self):
        """
        Tests that a pack can be sorted by rarity.
        """ 
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 'DGM.txt')
        expansion = parse_expansion_file(expansion_txt_file_location)
        pack = expansion.generate_pack()
        self.assertEqual(len(pack.cards), 14)
        self.assertEqual(len(pack.commons), 10)
        self.assertEqual(len(pack.uncommons), 3)
        self.assertEqual(len(pack.rares), 1)
