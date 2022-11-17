// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// simple pseudo code:
// R2 = 0
// for cnt in range(R0):
//     R2 += R1

// detailed pseudo code:
// R2 = 0
// cnt = 0
// while True:
//     if (cnt - R0) == 0:
//         break
//     R2 = R2 + R1
//     cnt = cnt + 1



(START)
    @R2
    M=0  // RAM[R2] = 0

    @cnt
    M=0  // RAM[cnt] = 0

(LOOP)
    @cnt
    D=M  // RegD = RAM[cnt]

    @R0
    D=D-M  // RegD = RegD - RAM[R0]

    @END
    D;JEQ  // goto END if RegD == 0

    @R1
    D=M  // RegD = RAM[R1]
    @R2
    M=M+D  // RAM[R2] = RAM[R2] + RegD

    @cnt
    M=M+1  // increase counter by 1

    @LOOP
    0;JMP  // repeat loop

(END)
    @END
    0;JMP 