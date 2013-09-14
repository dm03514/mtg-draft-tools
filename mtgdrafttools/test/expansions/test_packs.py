import unittest

from mtgdrafttools.expansions.utils import get_expansion

class TextPacks(unittest.TestCase):
   
    def test_pack_filter_by_rarity(self):
        """
        Tests that a pack can be sorted by rarity.
        """ 
        expansion = get_expansion('dgm')

        pack = expansion.generate_pack()
        self.assertEqual(len(pack.cards), 14)
        self.assertEqual(len(pack.commons), 10)
        self.assertEqual(len(pack.uncommons), 3)
        self.assertEqual(len(pack.rares), 1)
