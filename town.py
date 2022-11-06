import kobold
import building
import event
import random

class Town:
    def __init__(self):
        self.add_kobolds()
        self.add_buildings()

    '''creates kobolds of an appropriate age. Should be changed to a more custom, balanced approach'''
    def add_kobolds(self):
        i = 0
        while(i < self.start_kobolds):
            self.kobolds.append(kobold.Kobold(random.randint(12, 30)))
            i = i+1

    '''this will in the future add all buildings from a json file'''
    def add_buildings(self):
        #todo, create a json document with buildings
        data_buildings = [{"type" : "wood",
                    "name" : "Sawmill",
                    "production": [["wood", 10]],
                    "description" : "A crude place for cutting wood",
                    "building_prereq" : [],
                    "building_material" : [["stone", 10]] ,
                    "event_text" : ["Work goes well"],
                    "production_freq" : 1 }]
        for data_building in data_buildings:
            self.buildings.append(building.Building(data_building["type"],
            data_building["name"], data_building["production"], data_building["description"], data_building["building_prereq"]
            , data_building["building_material"], data_building["event_text"], data_building["production_freq"]))

    '''todo, add a function for updating the building list from the json file'''

    '''adds events to the temporary list, used for events that generate new events'''
    def temp_add_event(self, event):
        self.temp_events.append(event)
    ''' Adds events to the regular event-list'''
    def add_event(self, event):
        self.events.append(event)
    '''adds and consumes resources through looking in the resource dict and getting an object of the type ["resource", amount]'''
    def add_resource(self, produced):
            self.resources[produced[0]] = self.resources[produced[0]] + produced[1]

    def subtract_resource(self, consumed):
            self.resources[consumed[0]] = self.resources[consumed[0]] - consumed[1]

    '''builds a building and adds its event to the queue'''
    def construct_building(self, building_index):
        #need a way to check that only buildnings that can get built get built in the website
        building_candidate = self.buildings[building_index]
        if building_candidate.get_level() == 0:
            cost = building_candidate.get_cost()
            for item in cost:
                self.subtract_resource(item)
            self.add_event(event.BuildingEvent(building_candidate, building_candidate.get_production_freq()))
            building_candidate.add_level()

    '''does the events'''
    def resolve_events(self):
        for event in self.events:
            event.do_event(self)
        self.events = self.temp_events
        self.temp_events = []

    '''adds text to the list of events to print.
    I am not quite sure of how to handle this, I probably need a more elegant way to make it look nice'''
    def add_event_text(self ,text):
        self.event_texts.append(text)



    start_kobolds = 6
    kobolds = []
    buildings = []
    events = []
    temp_events = []
    event_texts = []
    resources = {"wood" : 0, "stone": 0}

test_town = Town()
for test_kobold in test_town.kobolds:
    print(test_kobold)


test_town_2 = Town()
test_town_2.add_buildings()
test_town_2.construct_building(0)
test_i = 0
test_town_2.resolve_events()
print(test_town_2.resources)
test_town_2.resolve_events()
print(test_town_2.resources)
while(test_i <  10):
    test_town_2.resolve_events()
    print(test_town_2.resources)
    test_i += 1
