`timer.py`: Just an event timer, nothing fancy


# Usage

~~~

log = timer.Log()
log.create_event('my_fancy_event')
log.create_event('my_other_event')

log.start('my_fancy_event')
# ... my fancy code
log.start('my_other_event')
# ... other code
log.stop('my_fancy_event')
# ... moar code
log.stop('my_other_event')

log.print_summary()

~~~

