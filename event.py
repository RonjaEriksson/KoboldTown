#import town

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

class BuildingEvent(Event):

    def do_event(self, town):
        self.event_tick = self.event_tick - 1
        if event_tick != 0:
            town.temp_add_event(self)
        else:
             event = event_cause.event()
             town.event_text(event[0])
             for production in event[1]:
                 town.resource_add(production)
             town.temp_add_event(self.event_cause, event_cause.production_freq)
