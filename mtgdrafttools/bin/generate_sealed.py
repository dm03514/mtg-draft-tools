import argparse

from mtgdrafttools.sealed.pool import generate_sealed_pool
from mtgdrafttools import serializers 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('block', choices=['rtr', 'm14'], 
                        help='the block to generate a sealed pool for')
    args = parser.parse_args()

    pool = generate_sealed_pool(args.block)

    print(serializers.serialize('mws', pool.cards))

    
if __name__ == '__main__':
    main()
