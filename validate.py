
def validate_memory(mem):
    if 0<=int(mem)<=65535:
        return True
    return False


def validate_data(data):
    if 0<= data <= 255:
        return True
    return False


def validate_reg(reg):
    if reg == 'A' or reg == 'B' or reg == 'C' or reg == 'D' or reg == 'E' or reg == 'H' or reg == 'L' or reg == 'M':
        return True
    else:return False

def validate_regPair(reg1, reg2):
    import registers
    try:
        if registers.reg_pair[reg1] == reg2:
            return True
        return False
    except:
        return False
