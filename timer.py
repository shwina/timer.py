import time
from prettytable import PrettyTable

class TimedEvent:

    def __init__(self):
        self.start_time = None
        self.stop_time = None
        self.started = False
        self.ended = False

    def start(self):
        self.start_time = time.time()
        self.started = True

    def stop(self):
        self.stop_time = time.time()
        self.ended = True
        
    def get_elapsed_time(self):
        if self.ended:
            return self.stop_time - self.start_time
        else:
            raise ValueError('Elapsed time unavailable for event that hasn''t ended')

class Log:

    def __init__(self):
        self.logDict = {}
        self.log_table = PrettyTable()
        self.log_table.field_names = ('Event name', 'Time taken')
        self.log_table.align = "l"

    def create_event(self, event_name):
        self.logDict[event_name] = TimedEvent()

    def start(self, event_name):
        if event_name in self.logDict:
            self.logDict[event_name].start()
        else:
            raise UnboundLocalError('No event {0}'.format(event_name))

    def stop(self, event_name):
        if event_name in self.logDict:
            if self.logDict[event_name].started:
                self.logDict[event_name].stop()
            else:
                raise ValueError('Event {0} not started'.format(event_name))
        else:
            raise UnboundLocalError('No event {0}'.format(event_name))

    def print_summary(self):
        for event_name in self.logDict:
            if self.logDict[event_name].stopped:
                self.log_table.add_row((event_name,
                    self.logDict[event_name].get_elapsed_time()))
                    
        print self.log_table.get_string(sortby='Time elapsed', reversesort=True)
