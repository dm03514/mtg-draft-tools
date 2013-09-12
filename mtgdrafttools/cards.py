

class Card(object):

    def __init__(self, **attributes):
        """
        Right now intialize instance properities for all key/values passed in 
        This was to keep the method signature small, is this horrible?
        """
        for key, value in attributes.items():
            setattr(self, key, value)

    def __repr__(self):
        """
        Call the str method so we can see the card name in the terminal.
        is this kosher?
        """
        return str(self)

    def __str__(self):
        return 'Card: {}'.format(self.name)
