
// init stack pointer:
@256
D=A
@SP
M=D

// push constant 10
@10
D=A
@SP
M=M+1
A=M-1
M=D

// pop local 0
@0
D=A
@LCL
A=M
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D

// push constant 21
@21
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 22
@22
D=A
@SP
M=M+1
A=M-1
M=D

// pop argument 2
@2
D=A
@ARG
A=M
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D

// pop argument 1
@1
D=A
@ARG
A=M
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D

// push constant 36
@36
D=A
@SP
M=M+1
A=M-1
M=D

// pop this 6
@6
D=A
@THIS
A=M
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D

// push constant 42
@42
D=A
@SP
M=M+1
A=M-1
M=D

// push constant 45
@45
D=A
@SP
M=M+1
A=M-1
M=D

// pop that 5
@5
D=A
@THAT
A=M
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D

// pop that 2
@2
D=A
@THAT
A=M
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D

// push constant 510
@510
D=A
@SP
M=M+1
A=M-1
M=D

// pop temp 6
@SP
M=M-1
A=M
D=M
@11
M=D

// push local 0
@0
D=A
@LCL
A=M
A=A+D
D=M
@SP
M=M+1
A=M-1
M=D

// push that 5
@5
D=A
@THAT
A=M
A=A+D
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

// push argument 1
@1
D=A
@ARG
A=M
A=A+D
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

// push this 6
@6
D=A
@THIS
A=M
A=A+D
D=M
@SP
M=M+1
A=M-1
M=D

// push this 6
@6
D=A
@THIS
A=M
A=A+D
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

// sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1

// push temp 6
@11
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
@227
0;JMP
