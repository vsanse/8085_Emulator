import registers
import validate


def setZero(result):
    if int(result,16) == 0:
        registers.flag.update({"Z":1})
    else:
        registers.flag.update({"Z":0})


def setCarry(result):
    if not validate.validate_data(result):
        registers.flag.update({"CY":1})
    else:
        registers.flag.update({"CY": 0})


def setParity(result):
    parity = result.count("1")
    if parity%2 == 0:
        registers.flag.update({"P":1})
    else:
        registers.flag.update({"P": 0})

def setAC(result):
    pass


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

def setFlags(result):
    result_bcd = bcd(result)
    setZero(result)
    setCarry(result)
    setParity(result_bcd)
    setAC(result)
    setSign(result_bcd)

setParity(bcd("12"))