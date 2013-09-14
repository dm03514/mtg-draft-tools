

class PoolBase(object):
    """
    Superclass for any pool of cards,
    """

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
