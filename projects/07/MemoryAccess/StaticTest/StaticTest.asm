
// init stack pointer:
@256
D=A
@SP
M=D

// push constant 111
@111
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 333
@333
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 888
@888
D=A
@SP
M=M+1
A=M-1
M=D

// pop static 8
@SP
M=M-1
A=M
D=M
@24
M=D

// pop static 3
@SP
M=M-1
A=M
D=M
@19
M=D

// pop static 1
@SP
M=M-1
A=M
D=M
@17
M=D

// push static 3
@19
D=M
@SP
M=M+1
A=M-1
M=D

// push static 1
@17
D=M
@SP
M=M+1
A=M-1
M=D

// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1

// push static 8
@24
D=M
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
@72
0;JMP
