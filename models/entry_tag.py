class EntryTag():

    """
    A class used to represent Entry Tag relationship
    """

    def __init__(self, id, entry_id, tag_id):
        """
        Parameters
        ----------
        entry_id : int
            pk id of an Entry
        tag_id : int
            pk id of a Tag
        """
        self.id = id
        self.entry_id = entry_id
        self.tag_id = tag_id
