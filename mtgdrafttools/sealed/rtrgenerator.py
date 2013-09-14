from mtgdrafttools.expansions.pools import Pool
from mtgdrafttools.expansions.utils import get_expansion
from .base_generator import BaseGenerator


class RTRSealedPoolGenerator(BaseGenerator):

    def gen_pool(self):
        """
        Generates an RTR pool.  This consists of 2 packs of gtc, rtr, and dgm
        @return Object `Pool` instance
        """
        expansion_abbrevs = ['dgm', 'rtr', 'gtc']
        NUM_PACKS_PER_EXPANSION = 2

        cards_list = []

        for expansion_abbrev in expansion_abbrevs:
            expansion = get_expansion(expansion_abbrev)
            for i in range(NUM_PACKS_PER_EXPANSION):
                cards_list.extend(expansion.generate_pack().cards)
        return Pool(cards_list)
