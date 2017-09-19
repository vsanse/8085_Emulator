import registers
import validate
import instruction_sizes


def read_program(mem):
    ip = open("input.asm", "r")
    for line in ip:
        print hex(mem),line,
        line = list(line.split(" "))
        mem += instruction_sizes.getSize(line[0])

    return mem


if __name__ == "__main__":
    mem = raw_input("Enter Memory Location to Start With:")
    mem_int = int(mem, 16)
    if validate.validate_memory(mem):
        read_program(mem_int)

    else:
        print "Enter Valid Memory"
