import debugger
import initialization
import registers


def start():
    query = raw_input("Do you want to start in DEBUGGER mode(y/n/q to quit): ")
    if query == 'y' or query == 'Y':
        registers.dBugOn = True
        debugger.startDebugger()

    elif query == 'N' or query == 'n':
        initialization.memInit()

    elif query == 'Q' or query == 'q':
        exit(1)

    else:
        print "invalid command. Please Retry!"
        start()


start()
