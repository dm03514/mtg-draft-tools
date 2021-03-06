import argparse

from mtgdrafttools import settings
from mtgdrafttools.expansions.utils import get_expansion
from mtgdrafttools import serializers 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('expansion', choices=settings.SUPPORTED_EXPANSION_PATHS.keys(),
                        help='the expansion to generate packs for')
    parser.add_argument('-np', '--num_packs', default=1, type=int,
                        help='(default: 1)')
    args = parser.parse_args()

    expansion = get_expansion(args.expansion)
    # make the appropriate number of packs
    # combine every card generated into a list of cards
    cards_list = []
    for i in range(args.num_packs):
        cards_list.extend(expansion.generate_pack().cards)

    # serialize the packs and print to stdout
    print(serializers.serialize('mws', cards_list))

if __name__ == '__main__':
    main()
