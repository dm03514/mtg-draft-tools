import os
import unittest

from mtgdrafttools import settings
from mtgdrafttools.expansions.cards import Card
from mtgdrafttools.expansions.utils import get_expansion
from mtgdrafttools.serializers.mws import MWSSerializer, MWSExpansionDeserializer


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


class TestMWSDeserializer(unittest.TestCase):

    def test_parse_expansion_file_into_cards(self):
        """
        Tests that given an expansion text file in the MWS format we 
        can get a set of cards from it.
        """
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 'DGM.txt')
        parser = MWSExpansionDeserializer(expansion_txt_file_location)
        expansion = parser.get_expansion()
        self.assertEqual(len(expansion.cards), 166)
    
    def test_parse_expansion_file_into_cards_include_basic_lands(self):
        """
        Make sure that basic lands are included in the expansion
        """
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 'M14.txt')
        parser = MWSExpansionDeserializer(expansion_txt_file_location, 
                                          include_basic_lands=True)
        expansion = parser.get_expansion()
        self.assertEqual(len(expansion.cards), 249)

    def test_parse_expansion_file_into_cards_no_basic_lands(self):
        """
        Make sure that basic lands are NOT included in the expansion 
        """
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 'M14.txt')
        parser = MWSExpansionDeserializer(expansion_txt_file_location)
        expansion = parser.get_expansion()
        self.assertEqual(len(expansion.cards), 229)

    def test_parse_card_multiple_card_text_lines_activated_ability(self):
        """
        Tests that when a card has multiple card text lines, all card text lines are
        associated as a list to the `card_text` key
        """
        card_lines_list = ['Pow/Tou:\t4/5', "Card Text:\t%U: Exile AEtherling. Return it to the battlefield under its owner's control at the beginning of the next end step.", '%U: AEtherling is unblockable this turn', '%1: AEtherling gets +1/-1 until end of turn.', '%1: AEtherling gets -1/+1 until end of turn.', 'Artist:\t\tTyler Jacobson']
        parser = MWSExpansionDeserializer('')
        card = parser._parse_card(card_lines_list)
        self.assertIsInstance(card, Card);
        self.assertEqual(card.text, ["%U: Exile AEtherling. Return it to the battlefield under its owner's control at the beginning of the next end step.", '%U: AEtherling is unblockable this turn', '%1: AEtherling gets +1/-1 until end of turn.', '%1: AEtherling gets -1/+1 until end of turn.'])

    def test_parse_card_multiple_card_text_lines_static_ability(self):
        """
        Tests that when a card has multiple card text lines, all card text lines are
        associated as a list to the `card_text` key. A static ability is like Flying,
        Battalion, etc
        """
        card_lines_list = ['Pow/Tou:\t3/6', 
                           'Card Text:\tVigilance', 'Multicolored creatures you control have vigilance.', 'Flavor Text: \tThe route has been known for millenia, but only by those with no means to tell it.', 
                           'Artist:\t\tYeong-Hao Han']
        parser = MWSExpansionDeserializer('')
        card = parser._parse_card(card_lines_list)
        self.assertIsInstance(card, Card);
        self.assertEqual(card.text, ['Vigilance', 'Multicolored creatures you control have vigilance.'])
