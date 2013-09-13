import argparse

from mtgdrafttools.expansionparser import parse_expansion_file, sort_by_rarity


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_expansion_txt')
    parser.add_argument('-np', '--num_packs', default=1, type=int)
    args = parser.parse_args()

    cards_list = parse_expansion_file(args.path_to_expansion_txt)

    import ipdb; ipdb.set_trace();

if __name__ == '__main__':
    main()
