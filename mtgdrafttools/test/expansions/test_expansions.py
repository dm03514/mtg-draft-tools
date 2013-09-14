import unittest

from mtgdrafttools.expansions.utils import get_expansion


class TextExpansions(unittest.TestCase):

    def test_filter_by_rarity(self):
        """
        Tests that cards in an expansion can be filtered by rarity.
        """
        expansion = get_expansion('dgm')
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
        expansion = get_expansion('dgm')
        cards_by_rarity = expansion._get_cards_by_rarity()
        for key in ['C', 'U', 'R']:
            self.assertTrue(key in cards_by_rarity)

    def test_generate_pack_for_dgm(self):
        """
        Test that a dragons maze pack can be generated successfully.
        """
        expansion = get_expansion('dgm')
        pack = expansion.generate_pack()
        self.assertEqual(len(pack.cards), 14)
        self.assertEqual(len(pack.commons), 10)
        self.assertEqual(len(pack.uncommons), 3)
        self.assertEqual(len(pack.rares), 1)
