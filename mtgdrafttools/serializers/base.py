from cStringIO import StringIO

from mtgdrafttools import settings
from mtgdrafttools.expansions.cards import Card
from mtgdrafttools.expansions.expansions import Expansion


class BaseSerializer(object):

    def __init__(self):
        self.output = StringIO()

    def serialize(self, cards_list):
        """
        Entry point for serialization.
        Serializes a list of card objects
        """
        self.cards = cards_list
        self._start_serialization()
        for card in self.cards:
            self._handle_card(card)

        self._end_serialization()
        return self.getvalue()

    def _end_serialization(self):
        """
        Method called after all cards have been handled.
        """
        pass

    def getvalue(self):
        """
        Wraps the output object's `getvalue` method
        """
        return self.output.getvalue() 

    def _handle_card(self, card):
        """
        Serializes and writes a single card
        """
        raise NotImplementedError('Subclasses of BaseSerializer must override')

    def _start_serialization(self):
        """
        Initializes the serialization process.
        """
        pass 


class BaseExpansionDeserializer(object):
    _expansion_classes = {
        #'dgm': DGMExpansion
    }
    
    def __init__(self, expansion_abbrev, include_basic_lands=False):
        """
        Right now just requires a string to a file to open,
        deserializer takes care of opening and parsing it
        @param path_to_file string
        """
        self.expansion_abbrev = expansion_abbrev
        self.path_to_file = settings.SUPPORTED_EXPANSION_PATHS[expansion_abbrev]
        self.include_basic_lands = include_basic_lands

    def get_expansion(self):
        """
        returns an `Expansion` instance for all cards in the 
        """
        with open(self.path_to_file) as f:
            cards_list = self._get_cards(f)
            if self.expansion_abbrev in self._expansion_classes:
                return self._expansion_classes[self.expansion_abbrev](cards_list)
            else:
                return Expansion(cards_list)

    def _get_cards(self, f):
        """
        get a list of all cards in the file
        """ 
        raise NotImplementedError('Return List of `Card` objects')
