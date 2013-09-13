import argparse

from mtgdrafttools.expansionparser import parse_expansion_file
from mtgdrafttools import serializers 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_expansion_txt')
    parser.add_argument('-np', '--num_packs', default=1, type=int)
    args = parser.parse_args()

    expansion = parse_expansion_file(args.path_to_expansion_txt)
    # make the appropriate number of packs
    # combine every card generated into a list of cards
    cards_list = []
    for i in range(args.num_packs):
        cards_list.extend(expansion.generate_pack().cards)

    # serialize the packs and print to stdout
    print(serializers.serialize('mws', cards_list))

if __name__ == '__main__':
    main()
