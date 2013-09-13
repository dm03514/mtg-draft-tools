# Responsible for generating packs


class Pack(object):

    def __init__(self, cards):
        self.cards = cards

    def _filter_by_rarity(self, rarity):
        """
        Filters the current cards by rarity symbol
        @rarity string 'R', 'U', 'C'
        @return list
        """
        return [card for card in self.cards if card.rarity == rarity]

    @property
    def rares(self):
        return self._filter_by_rarity('R')

    @property
    def uncommons(self):
        return self._filter_by_rarity('U')

    @property
    def commons(self):
        return self._filter_by_rarity('C')

    def __repr__(self):
        """
        Call the str method
        Is this a no no??
        """
        return str(self)

    def __str__(self):
        return '<Pack: {} cards>'.format(len(self.cards))
