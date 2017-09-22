import debugger
import initialization
import registers


def start(isCmdLine=False):
    query = raw_input("Do you want to start in DEBUGGER mode(y/n/q to quit): ")
    if query == 'y' or query == 'Y':
        registers.dBugOn = True
        debugger.startDebugger(isCmdLine=isCmdLine)

    elif query == 'N' or query == 'n':
        initialization.memInit(isCmdLine=isCmdLine)

    elif query == 'Q' or query == 'q':
        exit(1)

    else:
        print "invalid command. Please Retry!"
        start()


if __name__ == "__main__":
    qw = raw_input("Do you wish to write program here(y/n for providing file name/q-quit):")
    if qw == 'y' or qw == 'Y':
        print "Please enter EOF to end writing(Make sure you have last command of program as HLT)"
        f = open('input.asm', 'w')
        while True:
            cmd = raw_input().strip()
            if cmd == "EOF":
                f.close()
                start(isCmdLine=True)
                break
            else:
                f.write(cmd + "\n")
    elif qw == 'q' or qw == 'Q':
        exit(1)

    else:
        start()
