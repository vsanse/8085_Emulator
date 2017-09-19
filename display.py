import registers

def show():
    print "_________Memory_____________"
    for addr,data in registers.memory.items():
        print addr,data
    print "____________________________\n\n"

    print "_________Registers__________"
    for reg,val in registers.reg.items():
        print reg,val
    print "____________________________\n\n"

    print "___________Flags____________"
    for f,val in registers.flag.items():
        print f,val
    print "____________________________\n\n"
