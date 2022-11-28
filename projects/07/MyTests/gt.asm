
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

// gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@TRUE.GT.0
D;JGT
D=0
@END.GT.0
0;JMP
(TRUE.GT.0)
D=-1
(END.GT.0)
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

// gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@TRUE.GT.1
D;JGT
D=0
@END.GT.1
0;JMP
(TRUE.GT.1)
D=-1
(END.GT.1)
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

// gt
@SP
A=M-1
D=M
A=A-1
D=M-D
@TRUE.GT.2
D;JGT
D=0
@END.GT.2
0;JMP
(TRUE.GT.2)
D=-1
(END.GT.2)
@SP
M=M-1
A=M-1
M=D

// add endless loop on program end:
@85
0;JMP
