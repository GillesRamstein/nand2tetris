
// function SimpleFunction.test 2
(SimpleFunction.test)
@LCL                // (0)  init local variables
A=M                 // (1)
M=0                 // (2)  init 1/2 local vars to 0
A=A+1               // (3)
M=0                 // (4)  init 2/2 local vars to 0
@SP                 // (5)  inc SP by 2 local vars
M=M+1               // (6)
M=M+1               // (7)

// push local 0
@0                  // (8)
D=A                 // (9)
@LCL                // (10)
A=M                 // (11)
A=A+D               // (12)
D=M                 // (13)
@SP                 // (14)
M=M+1               // (15)
A=M-1               // (16)
M=D                 // (17)

// push local 1
@1                  // (18)
D=A                 // (19)
@LCL                // (20)
A=M                 // (21)
A=A+D               // (22)
D=M                 // (23)
@SP                 // (24)
M=M+1               // (25)
A=M-1               // (26)
M=D                 // (27)

// add
@SP                 // (28)
A=M-1               // (29)
D=M                 // (30)
A=A-1               // (31)
M=M+D               // (32)
@SP                 // (33)
M=M-1               // (34)

// not
@SP                 // (35)
A=M-1               // (36)
M=!M                // (37)

// push argument 0
@0                  // (38)
D=A                 // (39)
@ARG                // (40)
A=M                 // (41)
A=A+D               // (42)
D=M                 // (43)
@SP                 // (44)
M=M+1               // (45)
A=M-1               // (46)
M=D                 // (47)

// add
@SP                 // (48)
A=M-1               // (49)
D=M                 // (50)
A=A-1               // (51)
M=M+D               // (52)
@SP                 // (53)
M=M-1               // (54)

// push argument 1
@1                  // (55)
D=A                 // (56)
@ARG                // (57)
A=M                 // (58)
A=A+D               // (59)
D=M                 // (60)
@SP                 // (61)
M=M+1               // (62)
A=M-1               // (63)
M=D                 // (64)

// sub
@SP                 // (65)
A=M-1               // (66)
D=M                 // (67)
A=A-1               // (68)
M=M-D               // (69)
@SP                 // (70)
M=M-1               // (71)

// return
// (from SimpleFunction.test to Sys.init)
@LCL                // (72)
A=M-1               // (73)  LCL-1
A=A-1               // (74)  LCL-2
A=A-1               // (75)  LCL-3
A=A-1               // (76)  LCL-4
A=A-1               // (77)  LCL-5
D=M                 // (78)  return_address from *LCL-5 to D
@13                 // (79)
M=D                 // (80)  store return_address in R13
@SP                 // (81)
A=M-1               // (82)
D=M                 // (83)  return_value from *SP-1 to D
@ARG                // (84)
A=M                 // (85)
M=D                 // (86)  store return_value in *ARG
D=A                 // (87)
@SP                 // (88)
M=D+1               // (89)  *SP = *ARG+1
@LCL                // (90)
M=M-1               // (91)  endFrame-1
A=M                 // (92)
D=M                 // (93)
@THAT               // (94)
M=D                 // (95)  restore THAT pointer
@LCL                // (96)
M=M-1               // (97)  endFrame-2
A=M                 // (98)
D=M                 // (99)
@THIS               // (100)
M=D                 // (101)  restore THIS pointer
@LCL                // (102)
M=M-1               // (103)  endFrame-3
A=M                 // (104)
D=M                 // (105)
@ARG                // (106)
M=D                 // (107)  restore ARG pointer
@LCL                // (108)
M=M-1               // (109)  endFrame-4
A=M                 // (110)
D=M                 // (111)
@LCL                // (112)
M=D                 // (113)  restore LCL pointer
@13                 // (114)
A=M                 // (115)  load return_address from R13
0;JMP               // (116)  jump to return_address
