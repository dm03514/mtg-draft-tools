import os

from mtgdrafttools.expansionparser import parse_expansion_file
from mtgdrafttools.sealed.base_generator import BaseGenerator

class RTRSealedPoolGenerator(BaseGenerator):

    def gen_pool(self):
        """
        Generates an RTR pool.  This consists of 2 packs of gtc, rtr, and dgm
        """
        script_location = os.path.abspath(os.path.dirname(__file__))
        expansion_files = ['DGM.txt', 'GTC.txt', 'RTR.txt']
        NUM_PACKS_PER_EXPANSION = 2

        cards_list = []
        script_location = os.path.abspath(os.path.dirname(__file__))

        for expansion_file in expansion_files:
            expansion_txt_file_location = os.path.join(script_location, '..', '..', 'data', expansion_file)
            expansion = parse_expansion_file(expansion_txt_file_location)
            for i in range(NUM_PACKS_PER_EXPANSION):
                cards_list.extend(expansion.generate_pack().cards)
        return cards_list

