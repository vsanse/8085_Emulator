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