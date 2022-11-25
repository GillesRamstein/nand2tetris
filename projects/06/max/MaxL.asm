// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/06/max/MaxL.asm

// Symbol-less version of the Max.asm program.

@0      // @R0
D=M
@1      // @R1
D=D-M
@10     // @OUTPUT_FIRST
D;JGT
@1      // @R1
D=M
@12     // @OUTPUT_D
0;JMP
    // (OUTPUT_FIRST)
@0      // @OUTPUT_FIRST
D=M
    // (OUTPUT_D)
@2      // @R2
M=D
    // (INFINITE_LOOP)
@14     // @INFINITE_LOOP
0;JMP
