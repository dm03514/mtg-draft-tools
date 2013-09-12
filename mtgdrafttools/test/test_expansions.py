import os
import unittest

from expansions import parse_expansion_file, _parse_card


class TestExpansions(unittest.TestCase):

    @unittest.skip('')
    def test_parse_expansion_file_into_cards(self):
        """
        Tests that given an expansion text file in the MWS format we 
        can get a set of cards from it.
        """
        script_location = os.path.abspath(os.path.dirname(__file__))
        expansion_txt_file_location = os.path.join(script_location, '..', '..', 'expansions', 'DGM.txt')
        cards_set = parse_expansion_file(expansion_txt_file_location)

    def test_parse_card_multiple_card_text_lines_static_ability(self):
        """
        Tests that when a card has multiple card text lines, all card text lines are
        associated as a list to the `card_text` key. A static ability is like Flying,
        Battalion, etc
        """
        card_lines_list = ['Card Name: \tAEtherling', 'Card Color:\tU', 'Mana Cost: \t4UU', 'Type & Class:\tCreature - Shapeshifter', 'Pow/Tou:\t4/5', "Card Text:\t%U: Exile AEtherling. Return it to the battlefield under its owner's control at the beginning of the next end step.", '%U: AEtherling is unblockable this turn', '%1: AEtherling gets +1/-1 until end of turn.', '%1: AEtherling gets -1/+1 until end of turn.', 'Artist:\t\tTyler Jacobson', 'Rarity: \tR', 'Card #:\t\t11/166']
        card = _parse_card(card_lines_list)
        import ipdb; ipdb.set_trace();
