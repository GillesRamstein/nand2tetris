
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

// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@TRUE.LT.0
D;JLT
D=0
@END.LT.0
0;JMP
(TRUE.LT.0)
D=-1
(END.LT.0)
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

// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@TRUE.LT.1
D;JLT
D=0
@END.LT.1
0;JMP
(TRUE.LT.1)
D=-1
(END.LT.1)
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

// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@TRUE.LT.2
D;JLT
D=0
@END.LT.2
0;JMP
(TRUE.LT.2)
D=-1
(END.LT.2)
@SP
M=M-1
A=M-1
M=D

// add endless loop on program end:
@85
0;JMP
