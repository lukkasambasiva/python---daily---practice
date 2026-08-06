 '''#car game
1.start
2.stop
3.exit'''
state = 'stop'
while True:
    print('1. start')
    print('2. stop')
    print('3. exit')
    ch=int(input('Choose a one optsion :'))
    match ch:
        case 1:
            if state=='stop':
                print('car is started')
                state ='start'
            else:
                print('car is already started')
        case 2:
             if state=='stop':
                 print('car is already stopped')
                 state = 'stop'
             else:
                 print('car is stoped')
        case 3:
            print('Exit')
            break
        case _:
            print('Choose correct opition')
