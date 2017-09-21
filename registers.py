from collections import OrderedDict as oDict

# REGISTERS
reg = oDict()
reg['A'] = '0'
reg['B'] = '0'
reg['C'] = '0'
reg['D'] = '0'
reg['E'] = '0'
reg['H'] = '0'
reg['L'] = '0'

# REGISTER PAIRS
reg_pair = oDict()
reg_pair['H'] = 'L'
reg_pair['B'] = 'C'
reg_pair['D'] = 'E'
reg_pair['A'] = 'F'

# FLAGS
flag = oDict()
flag['S'] = 0
flag['Z'] = 0
flag['AC'] = 0
flag['P'] = 0
flag['CY'] = 0

# COUNTERS
PC = 0
SP = 0

# MEMORY
memory = oDict()

# LABELS
label = oDict()

# DEBUGGER

dBugOn = False
