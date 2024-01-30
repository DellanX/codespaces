# Waiting Game
import random
import time
# 1. Generate a random number
target = random.randrange(1, 10)
# 2. Display the number to the user, and prompt the user to press enter to continue
print(f"Target Time {target}")
confirm = input('Press Enter to start')
start = time.time()
# 3. When the user presses enter the second time, stop the timer
terminate = input('Press Enter to stop')
stop = time.time()
# 4. When the timer is stopped, display to the user the elapsed time and how far off target they were
delta = stop - start
error = delta - target
print(f'Stopped after {delta:.3f}')
errorMessage = 'on target' if error == 0 else f'the error was {error:.3f} too slow' if error > 0 else f'the error was {-error:.3f} too fast'
print(f'Expected {target}, {errorMessage}')