import time
import timer
from nose.tools import assert_raises


def assert_allclose(a, b, rtol=1e-7):
    assert( abs((a-b)/a) <= rtol)

class TestLogging:

    def setup(self):
        self.log = timer.Log()

    def test_single_event(self):
        for sleep_time in [1e-3, 1e-2, 1e-1]:
            self.log.create_event('event_1')
            self.log.start('event_1')
            time.sleep(sleep_time)
            self.log.stop('event_1')
            assert_allclose(self.log.logDict['event_1'].stop_time - self.log.logDict['event_1'].start_time, sleep_time, rtol=0.1)

    def test_nested_events(self):
        self.log.create_event('event_1')
        self.log.create_event('event_2')

        self.log.start('event_1')
        time.sleep(1e-3)
        self.log.start('event_2')
        time.sleep(1e-3)
        self.log.stop('event_1')
        self.log.stop('event_2')

        assert_allclose(self.log.logDict['event_1'].stop_time - self.log.logDict['event_1'].start_time, 2e-3, rtol=0.1)
        assert_allclose(self.log.logDict['event_2'].stop_time - self.log.logDict['event_2'].start_time, 1e-3, rtol=0.1)
       
    def test_start_without_create(self):
        assert_raises(UnboundLocalError, self.log.start, 'event_nonexistent')

    def test_stop_without_create(self):
        assert_raises(UnboundLocalError, self.log.stop, 'event_nonexistent')

    def test_stop_without_start(self):
        self.log.create_event('event_1')
        assert_raises(ValueError, self.log.stop, 'event_1')
