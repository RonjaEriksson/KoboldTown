import kobold
import building
import event
import random

class Town:
    def __init__(self):
        self.add_kobolds()
        self.add_buildings()

    def add_kobolds(self):
        i = 0
        while(i < self.start_kobolds):
            self.kobolds.append(kobold.Kobold(random.randint(12, 30)))
            i = i+1

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

        def temp_add_event(self, event):
            temp_events.append(event)

        def add_event(self, event):
            events.append(event)

        def add_resource(self, production):
            for produced in production:
                resources[produced[0]] = resources[produced[0]] + produced[1]

        def subtract_resource(self, consumption):
            for consumed in consumption:
                resources[consumed[0]] = resources[consumed[0]] - consumed[1]

        def build_building(self, building_index):
            #need a way to check that only buildnings that can get built get built in the website
            building_candidate = self.buildings[building_index]
            if building_candidate.get_level() == 0:
                cost = building_candidate.get_cost()
                self.subtract_resource(cost)
                self.add_event(event.Event(building_candidate, building_candidate.get_production_freq()))
                building_candidate.add_level()


    start_kobolds = 6
    kobolds = []
    buildings = []
    events = []
    temp_events = []
    resources = {"wood" : 0, "stone": 0}

test_town = Town()
for kobold in test_town.kobolds:
    print(kobold)


test_town_2 = Town()
test_town.build_building(0)
