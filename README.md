<a class="zip_download_link" href="https://github.com/vishu-chaudhary/8085_Emulator/zipball/master">Download this project as a .zip file</a>
<a class="tar_download_link" href="https://github.com/vishu-chaudhary/8085_Emulator/tarball/master">Download this project as a tar.gz file</a>
# 8085-Emulator
Simulator for 8085 which supports 25 most commonly used commands which are -  
Load and Store - MOV , MVI , LXI , LDA , STA , LHLD , SHLD , STAX , XCHG  
Arithmetic - ADD , ADI , SUB , INR , DCR , INX , DCX , DAD , SUI  
Logical - CMA , CMP  
Branching - JMP , JC , JNC , JZ , JNZ  
One Additional command SET has been made to set data into valid memory locations (Eg - SET 2500,0A )  
The program will display contents of Registers A,B,C,D,E,H,L , flag Registers and used memory Locations only

## How This Works
Emulator uses python-2 as a backend to perform all operations.
Registers as well as flags and memory is taken as ordered dictionary.
### To run program:
$ python emulator.py
