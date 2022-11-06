import random
class Building:
    def __init__(self, type, name, production, description, building_prereq, building_material, event_text, production_freq):
        self.type = type
        self.name = name
        self.production = production
        self.description = description
        self.building_prereq = building_prereq
        self.building_material = building_material
        self.event_text = event_text
        self.production_freq = production_freq

    def event(self):
        return ( random.choice(self.event_text), self.production, self.production_freq)

    def get_level(self):
        return self.level

    def get_cost(self):
        return self.building_material

    def get_production_freq(self):
        return self.production_freq

    def add_level(self):
        self.level = self.level + 1

    #string of what category the building is in
    type = "none"
    #name of the building
    name = "name"
    #what level the building is, 0 is not built
    level = 0
    #A nested list of what the building produces in the forn ["resource", amount]
    production = []
    #how many tics are between every time the building produces
    production_freq = 1
    #flavourtext
    description = "description"
    #whether or not the building is shown as an option to build, used to keep some mystique about late game buildings
    visible = False
    #what reqiuerments must be met for the building to be visible.
    '''I am not sure how to do this. Maybe have categories and for the categories do a different sort of check.
    Like a dict with a category for science and a list of sciences that must be researched, a list of buildings that must be built, and an amount of kobolds that must exist
    so in the science category the list of research is compared to'''
    visible_req = "visible req"
    #what things must be researched, built or exist for this building to be buildable. Done the same as visible reqs.
    building_prereq = []
    #what is consumed when the building is built. A list of lists in the form forn ["resource", amount]
    building_material = []
    #A nested list of things that can be written when the building produces resources
    event_text = []
