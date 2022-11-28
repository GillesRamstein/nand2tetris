
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

// push constant 11
@11
D=A
@SP
M=M+1
A=M-1
M=D

// add
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1

// add endless loop on program end:
@23
0;JMP
