from mtgdrafttools.expansions.pools import Pool
from mtgdrafttools.expansions.utils import get_expansion
from .base_generator import BaseGenerator


class M14SealedPoolGenerator(BaseGenerator):

    def gen_pool(self):
        """
        Generate a sealed (6 pack m2014 pool)
        @return Object `Pool` instance
        """
        expansion = get_expansion('m14')

        cards_list = []
        NUM_PACKS_IN_POOL = 6
        for i in range(NUM_PACKS_IN_POOL):
            cards_list.extend(expansion.generate_pack().cards)
        return Pool(cards_list)
