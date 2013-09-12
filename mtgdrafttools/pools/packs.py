# Responsible for generating packs
from random import choice


class Pack(object):

    def __init__(self, cards):
        self.cards = cards

    @property
    def rares(self):
        return [card for card in self.cards if card.rarity == 'R']

    @property
    def uncommons(self):
        return [card for card in self.cards if card.rarity == 'U']

    @property
    def commons(self):
        return [card for card in self.cards if card.rarity == 'C']

    def __repr__(self):
        """
        Call the str method
        Is this a no no??
        """
        return str(self)

    def __str__(self):
        return 'Pack: {} cards'.format(len(self.cards))


def generate_pack(expansion_by_rarity):
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

    @param expansion_by_rarity dict with keys 'common', 'uncommon', 'rare' and set
        of cards with that rarity.  Lands will not be included and neither will 
        the rule cards
    @return list of cards
    """
    cards_in_pack = []
    # get one rare
    cards_in_pack.append(choice(expansion_by_rarity['R']))
    # get 3 uncommons
    for i in range(3):
        cards_in_pack.append(choice(expansion_by_rarity['U']))
    # get 10 commons
    for i in range(10):
        cards_in_pack.append(choice(expansion_by_rarity['C']))
    return Pack(cards_in_pack)



