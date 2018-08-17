def elevator():
    floor1 = int(input('Enter current floor:'))
    floor2 = int(input('Enter your floor:'))
    if (floor2 - floor1) <= 3:
        print('Go to floor:', floor2)
    else:
        print('Go to the ground floor')

elevator()
