import registers


def show():
    print "____________________________"
    print "_________Memory_____________"
    for addr,data in registers.memory.items():
        if data.strip().split(" ")[0] == "HLT":print addr,data+"\n"
        else:print addr,data
    print "____________________________"

    print "_________Registers__________"
    for reg,val in registers.reg.items():
        print reg,val
    print "____________________________"

    print "___________Flags____________"
    for f,val in registers.flag.items():
        print f,val
    print "____________________________"


    print "___________Labels___________"
    for l, val in registers.label.items():
        print l, val
    print "____________________________"
