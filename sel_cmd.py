import functions
import display
import registers
import instruction_sizes
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
        exit(1)


def start_exec(mem):

    while True:
        cmd = registers.memory.get(mem)
        t = cmd.strip().split(" ")
        mem_int = int(mem, 16)
        mem_int+=instruction_sizes.getSize(t[0])
        mem = format(mem_int, "0x")
        select(cmd)
