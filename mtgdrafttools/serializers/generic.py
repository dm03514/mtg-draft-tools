from collections import Counter

from .base import BaseSerializer


class GenericSerializer(BaseSerializer):
    """
    Serializes a list of cards into format of 
    {{ num_copies }} {{ Card Name }}
    """

    def _start_serialization(self):
        """
        Remove duplicate cards and keeps track of quantity.
        """
        cards_count = Counter(self.cards)
        # add the count as a property of cards
        cards_list = []
        for card, num_copies in cards_count.items():
            card.num_copies = num_copies
            cards_list.append(card)
        # replace the cards property with the cards including the num_copies
        self.cards = cards_list

    def _handle_card(self, card):
        """
        Serializes a specific card.
        """
        self.output.write('{} {}\n'.format(card.num_copies, card.name))
