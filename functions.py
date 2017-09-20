import registers
import validate
import set_flags


def ADD(reg):
    a = int(registers.reg.get("A"),16)
    b = int(registers.reg.get(reg),16)
    t = a + b
    if not validate.validate_data(t):
        print "\n////-----OverFlow Detected----////\n"
        t = format(t,"02x")
        set_flags.setCarry(t)
        set_flags.setFlags(a,b,t[1:],isAbnormalFlow=True)
        tmp = {"A": t[1:]}
    else:
        t = format(t, "02x")
        tmp = {"A": t}
        set_flags.setFlags(a,b,t)
    registers.reg.update(tmp)


def SUB(reg):
    a = int(registers.reg.get("A"),16)
    b = int(registers.reg.get(reg),16)
    t = a - b
    if not validate.validate_data(t):
        print "\n////-----UnderFlow Detected----////\n"
        t = format(t,"02x")
        set_flags.setCarry(t)
        set_flags.setFlags(a, b, t[1:], isAbnormalFlow=True)
        tmp = {"A": t[1:]}
    else:
        t = format(t, "02x")
        set_flags.setFlags(t)
        tmp = {"A": t}
        set_flags.setFlags(a,b,t)
    registers.reg.update(tmp)


def MOV(reg1, reg2):
    t = registers.reg.get(reg2)
    tmp = {reg1: t}
    registers.reg.update(tmp)


def LDA(addr):
    while True:
        data = raw_input("Enter Data At Memory Location %d: " % addr)
        if validate.validate_data(int(data,16)):
            tmp = {addr: data}
            registers.memory.update(tmp)
            registers.reg.update({"A": data})
            break
        else:
            print "Data Invalid. Please Retry"


def STA(addr):
    t = registers.reg.get("A")
    registers.memory.update({addr:t})


def HLT():
    return False
