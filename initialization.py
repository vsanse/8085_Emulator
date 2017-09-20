import sel_cmd
import validate
import registers
import instruction_sizes
import display
def read_program(mem):
    ip = open("input.asm", "r")
    for line in ip:
        # sel_cmd.select(line)
        mem_int = int(mem,16)
        t = line.strip().split(" ")
        if len(t) == 3 and t[0][-1:] == ":":
            registers.label.update({t[0][:-1]:mem})
            registers.memory.update({mem:(t[1]+" "+t[2])})
            mem_int+=instruction_sizes.getSize(t[1])
            mem = format(mem_int,"0x")
        elif len(t) == 2 or len(t) == 1:
            registers.memory.update({mem:line.strip()})
            mem_int += instruction_sizes.getSize(t[0])
            mem = format(mem_int, "0x")



def memInit():
    while True:
        mem = raw_input("Enter Memory Location to Start With:")
        # mem_int = int(mem, 16)
        if validate.validate_memory(mem):
            read_program(mem)
            break

        else:
            print "Enter Valid Memory!!"
