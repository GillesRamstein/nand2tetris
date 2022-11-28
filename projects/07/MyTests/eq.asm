
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

// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D

// eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@TRUE.EQ.0
D;JEQ
D=0
@END.EQ.0
0;JMP
(TRUE.EQ.0)
D=-1
(END.EQ.0)
@SP
M=M-1
A=M-1
M=D

// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D

// eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@TRUE.EQ.1
D;JEQ
D=0
@END.EQ.1
0;JMP
(TRUE.EQ.1)
D=-1
(END.EQ.1)
@SP
M=M-1
A=M-1
M=D

// push constant 8
@8
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 7
@7
D=A
@SP
M=M+1
A=M-1
M=D

// eq
@SP
A=M-1
D=M
A=A-1
D=M-D
@TRUE.EQ.2
D;JEQ
D=0
@END.EQ.2
0;JMP
(TRUE.EQ.2)
D=-1
(END.EQ.2)
@SP
M=M-1
A=M-1
M=D

// add endless loop on program end:
@85
0;JMP
