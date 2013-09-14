from collections import defaultdict
from random import choice

from mtgdrafttools.expansions.packs import Pack
from mtgdrafttools.expansions.pools import PoolBase


class Expansion(PoolBase):
    """
    Contains all the card in the expansions.
    Provides methods for generating packs.
    """

    def __init__(self, cards):
        """
        @param cards list of `Card` objects
        """
        self.cards = cards

    def generate_pack(self):
        """
        Generates a pack of data for a given expansion. 
        
        Currently a pack has:
            1 rare
            3 uncommons
            10 commons
            1 basic land/playercard
            1 token
        this function ignores the land and token
        also of note instead of a basic land DGM provides a dual land
        right now this function does not have custom cases per expansion it just
        generalizes to 1/3/10 ratio

        Current packs allow for duplicate cards...
        There are all sorts of tricky things involved with generating packs! 
        Mythics have been ignored too.... they are just considered rares
        """
        cards_in_pack = []
        cards_by_rarity = self._get_cards_by_rarity()
        # get one rare
        cards_in_pack.append(choice(cards_by_rarity['R']))
        # get 3 uncommons
        for i in range(3):
            cards_in_pack.append(choice(cards_by_rarity['U']))
        # get 10 commons
        for i in range(10):
            cards_in_pack.append(choice(cards_by_rarity['C']))
        return Pack(cards_in_pack)

    def _get_cards_by_rarity(self):
        """
        Group the cards by their rarity.
        @return dict with keys equal to the rarities in the input file 'C', 'U', 'R'
            each containing a list of cards with that rarity
        """
        cards_by_rarity = defaultdict(list)
        for card in self.cards:
            cards_by_rarity[card.rarity].append(card)
        return cards_by_rarity
