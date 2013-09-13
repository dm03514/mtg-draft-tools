from cStringIO import StringIO


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
        return self._getvalue()

    def _end_serialization(self):
        """
        Method called after all cards have been handled.
        """
        pass

    def _getvalue(self):
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

