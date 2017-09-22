import registers
import validate

def getPair(reg1, reg2):
    if validate.validate_regPair(reg1,reg2):
        data1 = registers.reg[reg1]
        data2 = registers.reg[reg2]
        if int(data1, 16) and data1 != "00" < 16:
            res = "0"+data1
        else:res = data1
        if int(data2, 16) and data2 != "00" < 16:
            res+=("0"+data2)
        else:res+= data2
        return res
    else:
        print "Invalid Register Pair",reg1, reg2
        exit(1)


def chkMemory(mem):
    try:
        registers.memory[mem]
        return True
    except:
        return False


def getLowerNibble(data):
    d = int(data, 16)
    d_bin = format(d, '08b')
    return d_bin[4:]


def chkLable(l):
    for key, val in registers.label.items():
        if key == l:
            return True
    return False
