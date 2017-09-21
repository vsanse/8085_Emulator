import instruction_sizes
import registers
import sel_cmd
import validate


def read_program(mem, count="", isCount=False):
    ip = open("input.asm", "r")
    hlt_mem = False
    for line in ip:
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
        elif len(t) == 2 or len(t) == 1:
            registers.memory[mem] = line.strip()
            mem_int += instruction_sizes.getSize(t[0])
            mem = format(mem_int, "0x")
            if t[0] == "HLT":
                hlt_mem = mem
                break

    if not hlt_mem:
        print "Please Add HLT Into Program!!!"
        exit(1)
    else:
        return hlt_mem


def memInit(count="", isCount=False, isStep=False):
    while True:
        mem = raw_input("Enter Memory Location to Start With:")
        # mem_int = int(mem, 16)
        if validate.validate_memory(mem):
            hlt_mem = read_program(mem, count, isCount)
            sel_cmd.start_exec(mem, isStep)
            break

        else:
            print "Enter Valid Memory!!"
