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
        return ( random.choice(self.event_text), production, production_freq)

    def get_level(self):
        return self.level

    def get_cost(self):
        return self.building_material

    def get_production_freq(self):
        return production_freq

    def add_level(self):
        self.level = self.level + 1

    type = "none"
    name = "name"
    level = 0
    production = []
    production_freq = 1
    description = "description"
    visible = False
    visible_req = "visible req"
    building_prereq = []
    building_material = []
    event_text = []
