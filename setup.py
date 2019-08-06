class student: 
    """
    represents the students to be scheduled
    """

    def __init__(self, name, ID, instrument, skill, avail, start, piano): 
        self.name = name
        self.ID = ID
        self.instrument = instrument
        self.skill = skill 
        self.avail = avail # list of strings 
        self.start = start 
        self.piano = piano 

class accompanist: 
    """
    represents each accompanist
    """
    
    booked_times = []
    booked_students = [] # sanity check for end, all students should be in these lists

    def __init__(self, name):
        self.name = name
