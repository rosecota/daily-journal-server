class Entry():

    """
    A class used to represent an Entry
    """

    def __init__(self, id, concept, entry, date, mood_id):
        """
        Parameters
        ----------
        concept : str
        entry : str
                Journal entry text the main point
        date : date
        mood_id : int
                the id of the mood associated around the entry
        mood
                None
        tags
                None
        """
        self.id = id
        self.concept = concept
        self.entry = entry
        self.date = date
        self.mood_id = mood_id
        self.mood = None
        self.tags = None
