import unittest

from mtgdrafttools.sealed.m14generator import M14SealedPoolGenerator
from mtgdrafttools.sealed.rtrgenerator import RTRSealedPoolGenerator


class TextSealedGenerators(unittest.TestCase):

    def test_m14_generate_sealed_pool(self):
        """
        Tests that a 84 card pool can be generated.
        """
        gen = M14SealedPoolGenerator()
        pool = gen.gen_pool()
        self.assertEqual(len(pool.cards), 84)

    def test_rtr_generate_sealed_pool(self):
        """
        Tests that a 84 card pool can be generated.
        """
        gen = RTRSealedPoolGenerator()
        pool = gen.gen_pool()
        self.assertEqual(len(pool.cards), 84)
