import extras
import registers
import set_flags
import validate


#####################################################
#                ARITHMETICS                        #
#####################################################

def ADD(register):
    if not validate.validate_reg(register):
        print "Invalid Register: %s"%register
        exit(1)
    a = int(registers.reg["A"], 16)
    if register == "M":
        b = extras.getPair('H', 'L')
        if extras.chkMemory(b):
            b = int(registers.reg[register], 16)
        else:
            print " Invalid Memory:", b
            exit(1)
    else:
        b = int(registers.reg[register], 16)
    t = a + b
    a = int(extras.getLowerNibble(format(a, '0x')), 2)
    b = int(extras.getLowerNibble(format(b, '0x')), 2)
    if not validate.validate_data(t):
        print "\n////-----OverFlow Detected----////\n"
        t = format(t,"02x")
        t = set_flags.setCarry(t)
        set_flags.setFlags(a, b, t, isAbnormalFlow=True)
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
    if register == "M":
        b = extras.getPair('H', 'L')
        if extras.chkMemory(b):
            b = int(registers.reg[register], 16)
        else:
            print " Invalid Memory:", b
            exit(1)
    else:
        b = int(registers.reg[register], 16)
    t = a - b
    a = int(extras.getLowerNibble(format(a, '0x')), 2)
    b = int(extras.getLowerNibble(format(b, '0x')), 2)
    if not validate.validate_data(t):
        print "\n////-----UnderFlow Detected----////\n"
        t = format(t,"02x")
        t = set_flags.setCarry(t)
        set_flags.setFlags(a, b, t, isAbnormalFlow=True)
        tmp = {"A": t[1:]}
    else:
        t = format(t, "02x")
        set_flags.setFlags(a, b, t)
        tmp = {"A": t}
        set_flags.setFlags(a,b,t)
    registers.reg.update(tmp)


def ADI(data):
    a = int(registers.reg['A'], 16)
    b = int(data, 16)
    res = format((a + b), '02x')
    a = int(extras.getLowerNibble(format(a, '0x')), 2)
    b = int(extras.getLowerNibble(format(b, '0x')), 2)
    if validate.validate_data(int(res, 16)):
        registers.reg['A'] = res
        set_flags.setFlags(a, b, res)
    else:
        print "\n Overflow Detected ADI", data
        print "Register Data[A]:", registers.reg['A']
        exit(1)


def INR(register):
    if validate.validate_reg(register):
        if register == 'M':
            a = extras.getPair('H', 'L')
            if extras.chkMemory(a):
                b = int(registers.memory[a], 16) + 1
                if b > 255:
                    b = 0
                registers.memory[a] = format(b, '0x')
            else:
                print "invalid memory:", a
                exit(1)
        else:
            b = int(registers.reg[register], 16) + 1
            if b > 255:
                b = 0
            registers.reg[register] = format(b, '0x')


def DCR(register):
    if validate.validate_reg(register):
        if register == 'M':
            a = extras.getPair('H', 'L')
            if extras.chkMemory(a):
                b = int(registers.memory[a], 16) - 1
                if b < 0:
                    b = 255
                registers.memory[a] = format(b, '0x')
            else:
                print "invalid memory:", a
                exit(1)
        else:
            b = int(registers.reg[register], 16) - 1
            if b < 0:
                b = 255
            registers.reg[register] = format(b, '0x')


def INX(reg1):
    if validate.validate_reg(reg1):
        try:
            reg2 = registers.reg_pair[reg1]
        except:
            print "invalid register pair", reg1
            exit(1)
        a = extras.getPair(reg1, reg2)
        a = int(a, 16) + 1
        if a > 65535:
            a = 0
        a = format(a, '04x')
        registers.reg[reg1] = a[:2]
        registers.reg[reg2] = a[2:]
    else:
        print "invalid register", reg1
        exit(1)


def DCX(reg1):
    if validate.validate_reg(reg1):
        try:
            reg2 = registers.reg_pair[reg1]
        except:
            print "invalid register pair", reg1
            exit(1)
        a = extras.getPair(reg1, reg2)
        a = int(a, 16) + 1
        if a < 0:
            a = 65535
        a = format(a, '04x')
        registers.reg[reg1] = a[:2]
        registers.reg[reg2] = a[2:]
    else:
        print "invalid register", reg1
        exit(1)


def DAD(reg1):
    if validate.validate_reg(reg1):
        c = 0
        try:
            reg2 = registers.reg_pair[reg1]
        except:
            print "invalid register pair", reg1
            exit(1)
        a = int(registers.reg[reg2], 16)
        res = int(registers.reg['L'], 16) + a
        if res > 255:
            c = 1
            res -= 256
        registers.reg['L'] = format(res, '02x')
        a = int(registers.reg[reg1], 16)
        res = int(registers.reg['H'], 16) + a + c
        res = format(res, '02x')
        if not validate.validate_data(int(res, 16)):
            res = set_flags.setCarry(res)
        registers.reg['H'] = res
    else:
        print 'invalid register pair:', reg1
        exit(1)


def SUI(data):
    a = int(registers.reg['A'], 16)
    b = int(data, 16)
    res = a - b
    res = format(res, '02x')
    if not validate.validate_data(int(res, 16)):
        res = set_flags.setCarry(res)
        set_flags.setFlags(a, b, res, isAbnormalFlow=True)
    else:
        set_flags.setFlags(a, b, res)

    registers.reg['A'] = res

#####################################################
#               LOAD AND STORE                      #
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
    data = registers.memory[addr]
    if validate.validate_data(int(data, 16)):
        registers.reg['A'] = data
    else:
        print "Data Invalid. Please Retry"

def STA(addr):
    registers.memory[addr] = registers.reg["A"]


def MVI(reg, data):
    if reg == 'M':
        a = extras.getPair('H','L')
        registers.memory[a] = data
    elif validate.validate_reg(reg):
        registers.reg[reg] = data
    else: print "Invalid Register"


def LXI(register, data):
    if validate.validate_reg(register):
        registers.reg[register] = data[:2]
        if len(data[2:]) > 1:
            registers.reg[registers.reg_pair[register]] = data[2:]
    else:
        print "Invalid Register",register
        exit(1)


def LHLD(addr):
    if extras.chkMemory(addr) and extras.chkMemory(str(int(addr) + 1)):
        registers.reg['L'] = registers.memory[addr]
        registers.reg['H'] = registers.memory[str(int(addr) + 1)]
    else:
        print "Pointing Invalid Memory:", addr


def SHLD(mem):
    a = extras.getPair('H', 'L')
    registers.memory[mem] = a


def XCHG():
    registers.reg['D'], registers.reg['H'] = registers.reg['H'], registers.reg['D']
    registers.reg['E'], registers.reg['L'] = registers.reg['L'], registers.reg['E']


def STAX(register):
    if validate.validate_reg(register):
        a = extras.getPair(register, registers.reg_pair[register])
        registers.memory[a] = registers.reg['A']
    else:
        print "Invalid Register:", register
        exit(1)


#####################################################
#               LOGICAL OPERATIONS                  #
#####################################################

def CMP(register):
    if validate.validate_reg(register):
        a_data = int(registers.reg['A'], 16)
        if register == 'M':
            a = extras.getPair('H', 'L')
            if validate.validate_memory(a):
                a = int(registers.memory[a], 16)
            else:
                print "Invalid Memory:", a
                exit(1)
        else:
            a = int(registers.reg[register], 16)
        if a_data < a:
            registers.flag['CY'] = 1
        elif a_data == a:
            registers.flag['Z'] = 1
        else:
            registers.flag['CY'] = 0
            registers.flag['Z'] = 0
    else:
        print "Invalid Register:", registers
        exit(1)


def CMA():
    data = registers.reg['A']
    registers.reg['A'] = format(255 - int(data, 16), '0x')


#####################################################
#            BRANCHING OPERATIONS                   #
#####################################################

def JMP(addr):
    if extras.chkLable(addr):
        return registers.label[addr]
    elif extras.chkMemory(addr):
        return addr
    else:
        print 'pointing to invalid memory:', addr
        exit(1)


def JC(addr):
    if registers.flag['CY'] == 1:
        return JMP(addr)
    else:
        return


def JNC(addr):
    if registers.flag['CY'] == 0:
        return JMP(addr)
    else:
        return


def JNZ(addr):
    if registers.flag['Z'] == 0:
        return JMP(addr)
    else:
        return


def JZ(addr):
    if registers.flag['Z'] == 1:
        return JMP(addr)
    else:
        return


#####################################################
#                   EXTRAS                          #
#####################################################

def SET(addr, data):
    if validate.validate_data(int(data,16)):
        registers.memory[addr] = data
    else:
        print "Data Invalid.\nPlease Enter Valid Data at Memory Location: %s"%addr
        exit(1)
