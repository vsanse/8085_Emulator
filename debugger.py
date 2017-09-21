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
    if validate.validate_reg(addr):
        print registers.reg[addr]

    elif extras.chkMemory(addr):
        print registers.memory[addr]

    else:
        print " Invalid Memory or Register!!"


def hlp():
    print "Setting BreakPoint          --------  break 3 or b 3"
    print "Run Program (or till BreakPoint) ---  run or r "
    print "Step by Step Execution      --------  step or s"
    print "Print Data From Register or Mem) ---  print A or p 2500"
    print "Quit Debugger               --------  quit or q"
    print "Show Available Commands     --------  help"


def step():
    initialization.memInit(isStep=True)


def run(breakPoint):
    if breakPoint > 0:
        initialization.memInit(count=breakPoint, isCount=True)
    else:
        initialization.memInit()


def startDebugger():
    while isDebuggerOn():
        cmd = raw_input("Enter Debugger Command: ").strip().split(" ")
        if cmd[0] == "break" or cmd[0] == "b":
            breakPoint = int(cmd[1])
        elif cmd[0] == "run" or cmd[0] == "r":
            run(breakPoint)
        elif cmd[0] == "step" or cmd[0] == "s":
            step()
        elif cmd[0] == "print" or cmd[0] == "p":
            prnt(cmd[1])
        elif cmd[0] == "help":
            hlp()
        elif cmd[0] == "quit" or cmd[0] == "q":
            registers.dBugOn = False
            return
        else:
            print "invalid command type help for list of commands!!"
