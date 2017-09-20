import sel_cmd
import validate
import registers
import instruction_sizes
import display


def read_program(mem):
    ip = open("input.asm", "r")
    hlt_mem = False
    for line in ip:
        # sel_cmd.select(line)
        mem_int = int(mem,16)
        t = line.strip().split(" ")
        if len(t) == 3 and t[0][-1:] == ":":
            registers.label[t[0][:-1]]=mem
            registers.memory[mem] = t[1]+" "+t[2]
            mem_int+=instruction_sizes.getSize(t[1])
            mem = format(mem_int,"0x")
        elif len(t) == 2 or len(t) == 1:
            if t[0] == "HLT":
                hlt_mem = mem
            registers.memory[mem] = line.strip()
            mem_int += instruction_sizes.getSize(t[0])
            mem = format(mem_int, "0x")
    if not hlt_mem:
        print "Please Add HLT Into Program!!!"
        exit(1)
    else:
        return hlt_mem


def memInit():
    while True:
        mem = raw_input("Enter Memory Location to Start With:")
        # mem_int = int(mem, 16)
        if validate.validate_memory(mem):
            hlt_mem = read_program(mem)
            sel_cmd.start_exec(mem)
            break

        else:
            print "Enter Valid Memory!!"
