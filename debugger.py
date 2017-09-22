import extras
import initialization
import registers
import validate

breakPoint = 0


def isDebuggerOn():
    if registers.dBugOn:
        return True
    else:
        return False


def prnt(addr):
    try:
        if validate.validate_reg(addr):
            print registers.reg[addr]

        elif extras.chkMemory(addr):
            print registers.memory[addr]

        else:
            print " Invalid Memory or Register!!"
    except:
        print "invalid command type help for list of commands!!"



def hlp():
    print "Setting BreakPoint          --------  break 3 or b 3"
    print "Run Program (or till BreakPoint) ---  run or r "
    print "Step by Step Execution      --------  step or s"
    print "Print Data From Register or Mem) ---  print A or p 2500"
    print "Quit Debugger               --------  quit or q"
    print "Show Available Commands     --------  help"


def step(isCmdLine=False):
    initialization.memInit(isStep=True, isCmdLine=isCmdLine)


def run(breakPoint, isCmdLine=False):
    if breakPoint > 0:
        initialization.memInit(count=breakPoint, isCount=True, isCmdLine=isCmdLine)
    else:
        initialization.memInit(isCmdLine=isCmdLine)


def startDebugger(isCmdLine=False):
    while isDebuggerOn():
        cmd = raw_input("Enter Debugger Command: ").strip().split(" ")
        if (cmd[0] == "break" or cmd[0] == "b") and len(cmd) > 1:
            breakPoint = int(cmd[1])
        elif cmd[0] == "run" or cmd[0] == "r":
            run(breakPoint, isCmdLine=isCmdLine)
        elif cmd[0] == "step" or cmd[0] == "s":
            step(isCmdLine=isCmdLine)
        elif (cmd[0] == "print" or cmd[0] == "p") and len(cmd) > 1:
            prnt(cmd[1])
        elif cmd[0] == "help":
            hlp()
        elif cmd[0] == "quit" or cmd[0] == "q":
            registers.dBugOn = False
            return
        else:
            print "invalid command type help for list of commands!!"
