# Program that displays each multiplication table when the user presses ENTER (time-delay)
# Written by Pavon Dunbar using Python v3.7.0

import time

for a in range(1,11):
    print('\n')
    time.sleep(2)
    for b in range(1,11):
        print(a, 'x' ,b, '=' , a*b)
        

print('Press ENTER to quit the application')

# END
