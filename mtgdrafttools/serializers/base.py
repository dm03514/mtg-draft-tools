from cStringIO import StringIO

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
    
    def __init__(self, path_to_file, include_basic_lands=False):
        """
        Right now just requires a string to a file to open,
        deserializer takes care of opening and parsing it
        @param path_to_file string
        """
        self.path_to_file = path_to_file
        self.include_basic_lands = include_basic_lands

    def get_expansion(self):
        """
        returns an `Expansion` instance for all cards in the 
        """
        with open(self.path_to_file) as f:
            cards_list = self._get_cards(f)
            return Expansion(cards_list)

    def _get_cards(self, f):
        """
        get a list of all cards in the file
        """ 
        raise NotImplementedError('Return List of `Card` objects')
