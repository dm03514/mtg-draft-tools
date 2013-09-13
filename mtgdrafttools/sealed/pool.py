from mtgdrafttools.sealed.rtrgenerator import RTRSealedPoolGenerator
from mtgdrafttools.sealed.m14generator import M14SealedPoolGenerator

def get_pool_generator(block_name):
    supported_blocks = {
        'rtr': RTRSealedPoolGenerator,
        'm14': M14SealedPoolGenerator
    }
    return supported_blocks[block_name]()


def generate_sealed_pool(block_name):
    """
    Generate a sealed pool for the block name
    @param block_name str 'rtr', or 'm14' right now
    @return list of cards in the pool.
    """
    pool_generator = get_pool_generator(block_name)
    return pool_generator.gen_pool()
