
// init stack pointer:
@256
D=A
@SP
M=D

// push constant 5
@5
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 3
@3
D=A
@SP
M=M+1
A=M-1
M=D

// or
@SP
A=M-1
D=M
A=A-1
M=M|D
D=A+1
@SP
M=M-1

// add endless loop on program end:
@24
0;JMP
