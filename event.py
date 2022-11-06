#import town

'''the base event class'''
class Event:
    def __init__(self, event_cause, event_tick):
        self.event_cause = event_cause
        self.event_tick = event_tick

    '''def do_event(self, town):
        self.event_tick = self.event_tick - 1
        if event_tick != 0
            town.add_event(self)
        else
            event_cause.event()'''

'''building event, the special thing about this is that it knows what a building spits out every tic'''
class BuildingEvent(Event):

    def do_event(self, town):
        self.event_tick = self.event_tick - 1
        if self.event_tick != 0:
            town.temp_add_event(self)
        else:
             event = self.event_cause.event()
             print(event)
             town.add_event_text(event[0])
             for production in event[1]:
                 town.add_resource(production)
             town.temp_add_event(BuildingEvent(self.event_cause, self.event_cause.production_freq))

'''todo! the big thing for events will probably be expeditions, so time to come back then'''
