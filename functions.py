import registers
import validate
import set_flags
import extras
import display


#####################################################
#                ARITHMETICS                        #
#####################################################

def ADD(register):
    if not validate.validate_reg(register):
        print "Invalid Register: %s"%register
        exit(1)
    a = int(registers.reg["A"],16)
    b = int(registers.reg[register],16)
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


def SUB(register):
    if not validate.validate_reg(register):
        print "Invalid Register: %s"%register
        exit(1)
    a = int(registers.reg["A"],16)
    b = int(registers.reg[register],16)
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


#####################################################
#  REGISTER-REGISTER | REGISTER-MEMORY MOVEMENT     #
#####################################################

def MOV(reg1, reg2):
    if not validate.validate_reg(reg1):
        print "Invalid Register: %s"%reg1
        exit(1)
    if not validate.validate_reg(reg2):
        print "Invalid Register: %s"%reg2
        exit(1)
    if reg1 == 'M':
        a = extras.getPair('H','L')
        if extras.chkMemory(a):
            registers.memory[a] = registers.reg[reg2]
        else: print " Invalid Memory:",a

    elif reg2 == 'M':
        a = extras.getPair('H', 'L')
        registers.reg[reg1] = registers.memory[a]
    else:
        registers.reg[reg1] = registers.reg[reg2]


def LDA(addr):
    while True:
        data = raw_input("Enter Data At Memory Location %d: " % addr)
        if validate.validate_data(int(data,16)):
            registers.memory[addr] = data
            registers.reg["A"]= data
            break
        else:
            print "Data Invalid. Please Retry"


def STA(addr):
    registers.memory[addr] = registers.reg["A"]


def MVI(reg, data):
    if reg == 'M':
        a = extras.getPair('H','L')
        if extras.chkMemory(a):
            registers.memory[a] = data
        else:
            print "Invalid Memory Location At H,L"
    elif validate.validate_reg(reg):
        registers.reg[reg] = data
    else: print "Invalid Register"

def LXI(register, data):
    if validate.validate_reg(register):
        registers.reg[register] = data[0:2]
        registers.reg[registers.reg_pair[register]] = data[2:]
    else:
        print "Invalid Register",register
        exit(1)


#####################################################
#                   EXTRAS                          #
#####################################################

def SET(addr, data):
    if validate.validate_data(int(data,16)):
        registers.memory[addr] = data
    else:
        print "Data Invalid.\nPlease Enter Valid Data at Memory Location: %s"%addr
        exit(1)


def HLT():
    return False
