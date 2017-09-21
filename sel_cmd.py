import display
import functions
import instruction_sizes
import registers


def select(cmd):
    cmd = cmd.strip().split(" ")
    if cmd[0] == "LDA":
        functions.LDA(int(cmd[1]))

    elif cmd[0] == "MOV":
        regs = cmd[1].strip().split(",")
        functions.MOV(regs[0], regs[1])

    elif cmd[0] == "STA":
        functions.STA(int(cmd[1]))

    elif cmd[0] == "MVI":
        operand = cmd[1].strip().split(",")
        functions.MVI(operand[0], operand[1])

    elif cmd[0] == "LXI":
        operand = cmd[1].strip().split(",")
        functions.LXI(operand[0],operand[1].strip())

    elif cmd[0] == "LHLD":
        functions.LHLD(cmd[1])

    elif cmd[0] == "SHLD":
        functions.SHLD(cmd[1])

    elif cmd[0] == "XCHG":
        functions.XCHG()

    elif cmd[0] == "STAX":
        functions.STAX(cmd[1])

    elif cmd[0] == "ADD":
        functions.ADD(cmd[1])

    elif cmd[0] == "SUB":
        functions.SUB(cmd[1])

    elif cmd[0] == 'CMP':
        functions.CMP(cmd[1])

    elif cmd[0] == 'CMA':
        functions.CMA()

    elif cmd[0] == "SET":
        operand = cmd[1].strip().split(",")
        functions.SET(operand[0], operand[1])

    elif cmd[0] == "HLT":
        display.show()
        exit(1)


def start_exec(mem):

    while True:
        cmd = registers.memory[mem]
        t = cmd.strip().split(" ")
        mem_int = int(mem, 16)
        mem_int+=instruction_sizes.getSize(t[0])
        mem = format(mem_int, "0x")
        select(cmd)
