# Responsible for generating packs

from mtgdrafttools.expansions.pools import PoolBase


class Pack(PoolBase):

    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        """
        Call the str method
        Is this a no no??
        """
        return str(self)

    def __str__(self):
        return '<Pack: {} cards>'.format(len(self.cards))
