// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// pseudo code:
// lastpixval = 1
// while True:
//     if KBD == 0:
//         pixval = 0
//     else:
//         pixval = 1
// 
//     if pixval == lastpixval:
//         continue
// 
//     address = SCREEN
//     while True:
//         if address == KBD:
//             break
//         value[address] = pixval
//         address += 16


(START)
    @lastpixval
    M=0

(MAINLOOP)
    @KBD
    D=M  // get keyboard register value into D

    @IF
    D;JEQ  // if keyboard==0 goto IF
    @ELSE
    0;JMP  // if keyboard!=0 goto ELSE

(IF)
    @pixval
    M=0

    @UPDATESCREEN
    0;JMP

(ELSE)
    @pixval
    M=-1

    @UPDATESCREEN
    0;JMP

(UPDATESCREEN)

    // return to mainloop if pixval did not change
    @lastpixval
    D=M
    @pixval
    D=D-M
    @MAINLOOP
    D;JEQ

    // set lastpixval = pixval
    @pixel
    D=M
    @lastpixval
    M=D

    // reset ptr to SCREEN
    @SCREEN
    D=A
    @ptr
    M=D

(SCREENLOOP)

    // return to mainloop if ptr = KBD (-> complete screen memory got traversed)
    @KBD
    D=A
    @ptr
    D=M-D
    @MAINLOOP
    D;JEQ

    // set ptr screen register to pixval
    @pixval
    D=M
    @ptr
    A=M
    M=D

    // increment pointer to next screen register
    @ptr
    M=M+1

    // next iteration in screen loop
    @SCREENLOOP
    0;JMP
