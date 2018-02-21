'''
PyAnnouncer
A Python library that easily lets
you output text that appears to be
generated in real-time by the machine!

Cyprien N, 2018
'''

from time import time
from random import randint, random

def delayed_announce(text, think=True):
    """Print text as if the computer was
    thinking to generate it.
    Words are seperated at spaces, and
    newlines are conserved.
    `think` controls whether or not a spinner
    is displayed while delaying output.
    It looks awesome!
    """

    sections = text.split(sep=' ')

    spinner = ['-', '\\', '|', '/']
    state = 0
    spin_delay = 0.1

    while sections:

        # Reset time, get new delay
        t0 = time()
        delay = randint(1, 3) * random()

        while (time() - t0) < delay:
            # While delay has not elapsed
            if think:
                # Print the spinner while waiting

                spin_t0 = time()
                while (time() - spin_t0) < spin_delay:
                    # Wait between spins
                    pass

                print(
                    '\b{}'.format(spinner[state]),
                    end='', sep='', flush=True
                )
                state += 1
                state %= 4

        # Delay is over, delete last spinner
        # charater, print current section,
        # and repeat
        print(
            '\b', sections.pop(0),
            end='  ', sep='', flush=True
        )

    print()


## A couple examples

delayed_announce(
    'I know who you are. I know where you are.'
)

# Use `+` and '\n' to format text
delayed_announce(
    'Hello, World! I am HAL9000.\n'
    + 'Just what do you think you\'re doing, Dave?'
)
