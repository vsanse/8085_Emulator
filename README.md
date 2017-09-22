<a class="zip_download_link" href="https://github.com/vishu-chaudhary/8085_Emulator/zipball/master">Download this project as a .zip file</a>
<a class="tar_download_link" href="https://github.com/vishu-chaudhary/8085_Emulator/tarball/master">Download this project as a tar.gz file</a>
# 8085-Emulator by Vishal Sanserwal
Simulator for 8085 which supports 25 most commonly used commands which are - <br> 
Load and Store - MOV , MVI , LXI , LDA , STA , LHLD , SHLD , STAX , XCHG   <br>
Arithmetic - ADD , ADI , SUB , INR , DCR , INX , DCX , DAD , SUI  <br>
Logical - CMA , CMP  <br>
Branching - JMP , JC , JNC , JZ , JNZ  <br>
One Additional command SET has been made to set data into valid memory locations (Eg - SET 2500,0A )  
#### Debugger
Program also has a debugger mode which you can select on the start of program.Currently it has following abilities:
<ul>
  <li><strong>break or b [line Number]</strong>: it will set break point on the given line number .</li>
<li><strong>run or r</strong>                : Run the program until it ends or breakoint is encountered.</li>
<li><strong>step or s</strong>               : It will run the program one instruction at a time.</li>
<li><strong>print or p [address or Register]</strong>: It prints the value of register or memory location for ex:<br>
 <strong>p A </strong>will print the value of register A.<br>
 <strong>p 2500</strong> will print the value at memory location x2500 if any.
  </li>
<li><strong>quit or q</strong>               : quit the debugger</li>
<li><strong>help</strong>: will show all the commands of debugger</li>
</ul>
TheThe program will display contents of Registers A,B,C,D,E,H,L , flag Registers and used memory Locations only

## How This Works
Emulator uses python-2 as a backend to perform all operations.
Registers as well as flags and memory is taken as ordered dictionary.<br>
<strong>Note:</strong> Make sure to end the program with "HLT" as final instruction for both command line as well as file mode.
#### How to write program
Make sure all the statements are in CAPS.<br>
For adding comments add '//' in start of instruction
###### Defining Label
<code>LABEL: OPERATION OPERAND</code><br>
<code>GO: ADD B</code>
###### Writing Program on Command Line (Command Line Mode)
Emulator has a mode to write program on terminal itself without providing file as input. This mode can be selected first time you start the emulator.<br>
<strong>Note:</strong> To exit the writing mode enter "EOF"

#### Sample Program
<code>//add 2 8 bit nos carry</code><br>
<code>LXI H,2500</code><br>
<code>MVI M,74</code><br>
<code>INX H</code><br>
<code>MVI M,AA</code><br>
<code>MVI C,00</code><br>
<code>LDA 2500</code><br>
<code>MOV B,A</code><br>
<code>LDA 2501</code><br>
<code>ADD B</code><br>
<code>JNC 2016</code><br>
<code>INR C</code><br>
<code>STA 2502</code><br>
<code>MOV A,C</code><br>
<code>STA 2503</code><br>
<code>HLT</code><br>

### To run program:
$ python emulator.py
