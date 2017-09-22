<a class="zip_download_link" href="https://github.com/vishu-chaudhary/8085_Emulator/zipball/master">Download this project as a .zip file</a>
<a class="tar_download_link" href="https://github.com/vishu-chaudhary/8085_Emulator/tarball/master">Download this project as a tar.gz file</a>
# 8085-Emulator
Simulator for 8085 which supports 25 most commonly used commands which are -  
Load and Store - MOV , MVI , LXI , LDA , STA , LHLD , SHLD , STAX , XCHG  
Arithmetic - ADD , ADI , SUB , INR , DCR , INX , DCX , DAD , SUI  
Logical - CMA , CMP  
Branching - JMP , JC , JNC , JZ , JNZ  
One Additional command SET has been made to set data into valid memory locations (Eg - SET 2500,0A )  
#### Debugger
Program also has a debugger mode which you can select on the start of program.Currently it has following abilities:
<pre>
break or b <line Number>: it will set break point on the given line number . <br>
run or r                : Run the program until it ends or breakoint is encountered.<br>
step or s               : It will run the program one instruction at a time.<br>
print or p              : It prints the value of register or memory location for ex p A will print the value of register A.<br>
                          p x2500 will print the value at memory location x2500 if any.<br>
quit or q               : quit the debugger<br>
help                    : will show all the commands of debugger<br>
print or p <address or Register> :The program will display contents of Registers A,B,C,D,E,H,L , flag Registers and used memory Locations only</pre>
## How This Works
Emulator uses python-2 as a backend to perform all operations.
Registers as well as flags and memory is taken as ordered dictionary.
### To run program:
$ python emulator.py
