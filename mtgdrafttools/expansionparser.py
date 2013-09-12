import itertools

from cards import Card


def parse_expansion_file(path):
    """
    Reads a MWS expansion text file into a set of Card objects.
    @param path string
    @return list of Card 
    """
    with open(path) as f:

        sections = _get_sections(f)
        return [_parse_card(card_lines_list) for card_lines_list in sections]


def _get_sections(f):
    """
    Sections are seperated by a blank line, this will yield each section as is
    without any cleaning.
    @param f Object open file
    @return yield
    """
    # Mws expansion file consists of cards seperated by an empty line
    # the header is the first section and contains metadata about the file
    # read until we get a newline then break
    current_section = []
    for line in f:
        line = line.strip()
        if line:
            current_section.append(line)
        else:
            yield current_section
            current_section = []
    else:
        # the file does not end with a new line make sure to yield
        # the last card
        yield current_section


def _parse_card(card_lines):
    """
    Converts a list of the card lines, as read from the file into a card object
    @param card_lines list
    @return Object Card instance
    """
    key_map = {
        'Card Name': 'name',
        'Card Color': 'color',
        'Mana Cost': 'mana_cost',
        'Type & Class': 'type_and_class',
        'Pow/Tou': 'power_toughness',
        'Card Text': 'text',
        'Rarity': 'rarity',
        'Card #': 'card_number',
        'Artist': 'artist',
        'Flavor Text': 'flavor_text'
    }
    card_data_dict = {}
    # the value in the file are seperated by a tab (\t) so strip that
    # and remap the keys
    last_key = None
    for line_str in card_lines:
        try:
            key, value = line_str.split(':') 

        except ValueError:
            # line can't be stripped, if last key was Card Text add it to the card text
            if last_key == 'Card Text':
                card_data_dict[key_map['Card Text']].append(line_str.strip())     
            elif line_str.startswith('Card Text:'):
                value = line_str.replace('Card Text:\t', '')
                card_data_dict[key_map['Card Text']] = [value.strip() or None]
                last_key = 'Card Text'
        else:
            # splitting was successfull make sure that the key is in the key map
            if key not in key_map.keys() and last_key == 'Card Text':
                card_data_dict[key_map['Card Text']].append(line_str.strip())
            elif key == 'Card Text':
                card_data_dict[key_map['Card Text']] = [value.strip() or None]
                last_key = key
            else:
                card_data_dict[key_map[key]] = value.strip() or None
                last_key = key

    return Card(**card_data_dict)
