

class Card(object):

    def __init__(self, **attributes):
        """
        Right now intialize instance properities for all key/values passed in 
        This was to keep the method signature small, is this horrible?
        """
        for key, value in attributes.items():
            setattr(self, key, value)
