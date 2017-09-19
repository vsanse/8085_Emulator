def getSize(cmd):
    if cmd == "MOV" or cmd == "ADD" or cmd == "SUB" or cmd == "XCHG" or cmd == "STAX" or cmd == "INR":
        return 1
    elif cmd == "INX" or cmd == "DCR" or cmd == "DCX" or cmd == "CMA" or cmd == "DAD" or cmd == "SET":
        return 1
    elif cmd == "CMP":
        return 1
    elif cmd == "MVI" or cmd == "ADI" or cmd == "SUI":
        return 2
    elif cmd == "LXI" or cmd == "LDA" or cmd == "LHLD" or cmd == "SHLD" or cmd == "STA":
        return 3
    elif cmd == "JMP" or cmd == "JC" or cmd == "JNC" or cmd == "JNZ" or cmd == "JZ":
        return 3
    else:
        return 0
