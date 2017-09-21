import display
import functions
import instruction_sizes
import registers

def select(cmd):
    cmd = cmd.strip().split(" ")
    #  LOAD AND STORE COMMANDS
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

    # ARITHMETIC COMMANDS

    elif cmd[0] == "ADD":
        functions.ADD(cmd[1])

    elif cmd[0] == "SUB":
        functions.SUB(cmd[1])

    elif cmd[0] == "ADI":
        functions.ADI(cmd[1])

    elif cmd[0] == "INR":
        functions.INR(cmd[1])

    elif cmd[0] == "DCR":
        functions.DCR(cmd[1])

    elif cmd[0] == "INX":
        functions.INX(cmd[1])

    elif cmd[0] == "DCX":
        functions.DCX(cmd[1])

    elif cmd[0] == "DAD":
        functions.DAD(cmd[1])

    elif cmd[0] == "SUI":
        functions.SUI(cmd[1])

    # LOGICAL COMMANDS

    elif cmd[0] == 'CMP':
        functions.CMP(cmd[1])

    elif cmd[0] == 'CMA':
        functions.CMA()

    # BRANCHING COMMANDS

    elif cmd[0] == 'JMP':
        return functions.JMP(cmd[1])

    elif cmd[0] == 'JC':
        return functions.JC(cmd[1])

    elif cmd[0] == 'JNC':
        return functions.JNC(cmd[1])

    elif cmd[0] == 'JZ':
        return functions.JZ(cmd[1])

    elif cmd[0] == 'JNZ':
        return functions.JNZ(cmd[1])

    # EXTRA COMMANDS

    elif cmd[0] == "SET":
        operand = cmd[1].strip().split(",")
        functions.SET(operand[0], operand[1])

    elif cmd[0] == "HLT":
        display.show()
        if registers.dBugOn == True:
            return
        exit(1)


def start_exec(mem, isStep=False):

    while True:
        cmd = registers.memory[mem]
        t = cmd.strip().split(" ")
        mem_int = int(mem, 16)
        mem_int+=instruction_sizes.getSize(t[0])
        mem = format(mem_int, "0x")
        if t[0] == "JMP" or t[0] == "JNC" or t[0] == "JC" or t[0] == "JZ" or t[0] == "JNZ":
            tmp_mem = mem
            mem = select(cmd)
            if mem is None:
                mem = tmp_mem
        else:
            select(cmd)
        if registers.dBugOn == True and cmd.strip() == "HLT":
            return
        if isStep:
            print "Executing:", cmd
            query = raw_input("Press Enter For Next Instruction Execution(q to quit step execution):")
            if query == "q" or query == "quit":
                return
