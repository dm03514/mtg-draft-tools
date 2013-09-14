from mtgdrafttools.expansions.utils import get_expansion
from mtgdrafttools.sealed.base_generator import BaseGenerator


class M14SealedPoolGenerator(BaseGenerator):

    def gen_pool(self):
        """
        Generate a sealed (6 pack m2014 pool)
        @return list of cards in the pool
        """
        expansion = get_expansion('m14')

        cards_list = []
        NUM_PACKS_IN_POOL = 6
        for i in range(NUM_PACKS_IN_POOL):
            cards_list.extend(expansion.generate_pack().cards)
        return cards_list
