import os
import unittest

from mtgdrafttools import settings
from mtgdrafttools.expansionparser import parse_expansion_file


class TextExpansions(unittest.TestCase):

    def test_filter_by_rarity(self):
        """
        Tests that cards in an expansion can be filtered by rarity.
        """
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 'DGM.txt')
        expansion = parse_expansion_file(expansion_txt_file_location)
        rarities_dict = {
            'rares': 'R',
            'uncommons': 'U',
            'commons': 'C'
        }
        for rarity, symbol in rarities_dict.items():
            cards_by_rarity = getattr(expansion, rarity)
            for card in cards_by_rarity:
                self.assertEqual(card.rarity, symbol)
    
    def test_get_cards_by_rarity(self):
        """
        Tests that an expansion can be successfully sorted by rarity.
        """
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
