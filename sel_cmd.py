import functions
import display

def select(cmd):
    cmd = cmd.strip().split(" ")
    if cmd[0] == "LDA":
        functions.LDA(int(cmd[1]))

    elif cmd[0] == "ADD":
        functions.ADD(cmd[1])

    elif cmd[0] == "SUB":
        functions.SUB(cmd[1])

    elif cmd[0] == "MOV":
        regs = cmd[1].strip().split(",")
        functions.MOV(regs[0], regs[1])

    elif cmd[0] == "STA":
        functions.STA(int(cmd[1]))

    elif cmd[0] == "HLT":
        display.show()

# def