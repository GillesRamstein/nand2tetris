
// init stack pointer:
@256
D=A
@SP
M=D

// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D

// neg
@SP
A=M-1
M=-M

// add endless loop on program end:
@13
0;JMP
