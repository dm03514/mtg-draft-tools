import os

from mtgdrafttools import settings
from mtgdrafttools.expansionparser import parse_expansion_file
from mtgdrafttools.sealed.base_generator import BaseGenerator


class M14SealedPoolGenerator(BaseGenerator):

    def gen_pool(self):
        """
        Generate a sealed (6 pack m2014 pool)
        @return list of cards in the pool
        """
        expansion_txt_file_location = os.path.join(settings.DATA_DIR, 'M14.txt')
        expansion = parse_expansion_file(expansion_txt_file_location)
        cards_list = []
        NUM_PACKS_IN_POOL = 6
        for i in range(NUM_PACKS_IN_POOL):
            cards_list.extend(expansion.generate_pack().cards)
        return cards_list
