import display
import functions
import instruction_sizes
import registers

def select(cmd):
    cmd = cmd.strip().split(" ")
    #  LOAD AND STORE COMMANDS
    if cmd[0] == "LDA" and len(cmd) > 1:
        functions.LDA(cmd[1])

    elif cmd[0] == "MOV" and len(cmd) > 1:
        regs = cmd[1].strip().split(",")
        functions.MOV(regs[0], regs[1])

    elif cmd[0] == "STA" and len(cmd) > 1:
        functions.STA(cmd[1])

    elif cmd[0] == "MVI" and len(cmd) > 1:
        operand = cmd[1].strip().split(",")
        functions.MVI(operand[0], operand[1])

    elif cmd[0] == "LXI" and len(cmd) > 1:
        operand = cmd[1].strip().split(",")
        functions.LXI(operand[0],operand[1].strip())

    elif cmd[0] == "LHLD" and len(cmd) > 1:
        functions.LHLD(cmd[1])

    elif cmd[0] == "SHLD" and len(cmd) > 1:
        functions.SHLD(cmd[1])

    elif cmd[0] == "XCHG":
        functions.XCHG()

    elif cmd[0] == "STAX" and len(cmd) > 1:
        functions.STAX(cmd[1])

    # ARITHMETIC COMMANDS

    elif cmd[0] == "ADD" and len(cmd) > 1:
        functions.ADD(cmd[1])

    elif cmd[0] == "SUB" and len(cmd) > 1:
        functions.SUB(cmd[1])

    elif cmd[0] == "ADI" and len(cmd) > 1:
        functions.ADI(cmd[1])

    elif cmd[0] == "INR" and len(cmd) > 1:
        functions.INR(cmd[1])

    elif cmd[0] == "DCR" and len(cmd) > 1:
        functions.DCR(cmd[1])

    elif cmd[0] == "INX" and len(cmd) > 1:
        functions.INX(cmd[1])

    elif cmd[0] == "DCX" and len(cmd) > 1:
        functions.DCX(cmd[1])

    elif cmd[0] == "DAD" and len(cmd) > 1:
        functions.DAD(cmd[1])

    elif cmd[0] == "SUI" and len(cmd) > 1:
        functions.SUI(cmd[1])

    # LOGICAL COMMANDS

    elif cmd[0] == 'CMP' and len(cmd) > 1:
        functions.CMP(cmd[1])

    elif cmd[0] == 'CMA':
        functions.CMA()

    # BRANCHING COMMANDS

    elif cmd[0] == 'JMP' and len(cmd) > 1:
        return functions.JMP(cmd[1])

    elif cmd[0] == 'JC' and len(cmd) > 1:
        return functions.JC(cmd[1])

    elif cmd[0] == 'JNC' and len(cmd) > 1:
        return functions.JNC(cmd[1])

    elif cmd[0] == 'JZ' and len(cmd) > 1:
        return functions.JZ(cmd[1])

    elif cmd[0] == 'JNZ' and len(cmd) > 1:
        return functions.JNZ(cmd[1])

    # EXTRA COMMANDS

    elif cmd[0] == "SET" and len(cmd) > 1:
        operand = cmd[1].strip().split(",")
        functions.SET(operand[0], operand[1])

    elif cmd[0] == "HLT":
        display.show()
        if registers.dBugOn == True:
            return
        exit(1)
    else:
        print "operand missing:", cmd
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
