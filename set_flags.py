import registers


def setZero(result):
    if int(result,16) == 0:
        registers.flag.update({"Z":1})
    else:
        registers.flag.update({"Z":0})


def setCarry(result):
    if int(result, 16) > 255:
        registers.flag.update({"CY":1})
        return format((int(result, 16) - 256), '0x')
    if int(result, 16) < 0:
        registers.flag.update({"CY": 1})
        return format((int(result, 16) + 256), '0x')
    else:
        registers.flag.update({"CY": 0})


def setParity(result):
    parity = result.count("1")
    if parity%2 == 0:
        registers.flag.update({"P":1})
    else:
        registers.flag.update({"P": 0})

def setAC(res1, res2):
    if res1+res2 > 15:
        registers.flag.update({"AC":1})
    else:
        registers.flag.update({"AC":0})


def setSign(result):
    if result[0] == "1":
        registers.flag.update({"S": 1})
    else:
        registers.flag.update({"S": 0})


def bcd(result):
    upperNibble = result[0]
    lowerNibble = result[1]
    uN_bin = format(int(upperNibble,16), "04b")
    lN_bin = format(int(lowerNibble, 16), "04b")
    return (uN_bin+lN_bin)

def setFlags(res1, res2, result, isAbnormalFlow = False):
    result_bcd = bcd(result)
    setZero(result)
    if not isAbnormalFlow:
        setCarry(result)
    setParity(result_bcd)
    setAC(res1,res2)
    setSign(result_bcd)
