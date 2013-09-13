import argparse

from mtgdrafttools.sealed.pool import generate_sealed_pool
from mtgdrafttools import serializers 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('block', choices=['rtr', 'm14'], 
                        help='the block to generate a sealed pool for')
    args = parser.parse_args()

    cards_list = generate_sealed_pool(args.block)
    import ipdb; ipdb.set_trace();

    print(serializers.serialize('mws', cards_list))

    
if __name__ == '__main__':
    main()
