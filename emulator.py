import sel_cmd
import validate


def read_program(mem):
    ip = open("input.asm", "r")
    for line in ip:
        sel_cmd.select(line)


if __name__ == "__main__":
    while True:
        mem = raw_input("Enter Memory Location to Start With:")
        mem_int = int(mem, 16)
        if validate.validate_memory(mem):
            read_program(mem_int)
            break

        else:
            print "Enter Valid Memory!!"
