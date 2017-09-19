def validate_memory(mem):
    if 0<=int(mem)<=65535:
        return True
    return False

def validate_data(data):
    if 0<= data <= 255:
        return True
    return False


