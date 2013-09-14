from .generic import GenericSerializer
from .base import BaseExpansionDeserializer
from mtgdrafttools.expansions.cards import Card


class MWSSerializer(GenericSerializer):
    """
    MWSSerializer IS a generic serializer, just a convenience class
    """
    pass


class MWSExpansionDeserializer(BaseExpansionDeserializer):
   
    def _get_cards(self, f):
        """
        Get a list of `Card` objects in the file
        """
        sections = self._get_sections(f)
        cards_list = [self._parse_card(card_lines_list) for card_lines_list in sections]

        # filter the cards that are not basic lands
        if not self.include_basic_lands:
            cards_list = [card for card in cards_list 
                            if 'Basic Land' not in card.type_and_class]
        return cards_list

    def _get_sections(self, f):
        """
        Generate all lines from the file associated with an individual card.
        Each card spans multiple lines in the file, this yields a list of strings
        Sections are seperated by a blank line, this will yield each section as is
        without any cleaning.
        @param f Object open file
        @return yield
        """
        # Mws expansion file consists of cards seperated by an empty line
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

    def _parse_card(self, card_lines):
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
