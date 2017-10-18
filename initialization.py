import instruction_sizes
import registers
import sel_cmd
import validate


def read_program(mem, count="", isCount=False, isCmdLine=False):
    if isCmdLine:
        file = "input.asm"
    else:
        file = raw_input("Enter program File path: ").strip()
    ip = open(file, "r")
    hlt_mem = False
    for line in ip:
        if line[0] == '\\':
            continue
        if isCount:
            if count > 0:
                count -= 1
            else:
                registers.memory[mem] = "HLT"
                hlt_mem = mem
                break
        mem_int = int(mem,16)
        t = line.strip().split(" ")
        if len(t) == 3 and t[0][-1:] == ":":
            registers.label[t[0][:-1]]=mem
            registers.memory[mem] = t[1]+" "+t[2]
            mem_int+=instruction_sizes.getSize(t[1])
            mem = format(mem_int,"0x")
        if len(t) ==2 and t[1] == "HLT":
            registers.label[t[0][:-1]] = mem
            registers.memory[mem] = t[1]
            hlt_mem = mem
            break
        elif len(t) == 2 or len(t) == 1:
            registers.memory[mem] = line.strip()
            mem_int += instruction_sizes.getSize(t[0])
            mem = format(mem_int, "0x")
            if t[0] == "HLT" or t[1] == "HLT":
                hlt_mem = mem
                break

    if not hlt_mem:
        print "Please Add HLT Into Program!!!"
        exit(1)
    else:
        return hlt_mem


def memInit(count="", isCount=False, isStep=False, isCmdLine=False):
    while True:
        mem = raw_input("Enter Memory Location to Start With:")
        # mem_int = int(mem, 16)
        if validate.validate_memory(mem):
            hlt_mem = read_program(mem, count, isCount, isCmdLine=isCmdLine)
            sel_cmd.start_exec(mem, isStep)
            break

        else:
            print "Enter Valid Memory!!"
