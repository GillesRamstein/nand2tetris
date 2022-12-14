
// push constant 0
@0                  // (0)
D=A                 // (1)
@SP                 // (2)
M=M+1               // (3)
A=M-1               // (4)
M=D                 // (5)

// pop local 0
@0                  // (6)
D=A                 // (7)
@LCL                // (8)
A=M                 // (9)
D=D+A               // (10)
@13                 // (11)
M=D                 // (12)
@SP                 // (13)
M=M-1               // (14)
A=M                 // (15)
D=M                 // (16)
@13                 // (17)
A=M                 // (18)
M=D                 // (19)

// label LOOP_START
(LOOP_START)

// push argument 0
@0                  // (20)
D=A                 // (21)
@ARG                // (22)
A=M                 // (23)
A=A+D               // (24)
D=M                 // (25)
@SP                 // (26)
M=M+1               // (27)
A=M-1               // (28)
M=D                 // (29)

// push local 0
@0                  // (30)
D=A                 // (31)
@LCL                // (32)
A=M                 // (33)
A=A+D               // (34)
D=M                 // (35)
@SP                 // (36)
M=M+1               // (37)
A=M-1               // (38)
M=D                 // (39)

// add
@SP                 // (40)
A=M-1               // (41)
D=M                 // (42)
A=A-1               // (43)
M=M+D               // (44)
@SP                 // (45)
M=M-1               // (46)

// pop local 0
@0                  // (47)
D=A                 // (48)
@LCL                // (49)
A=M                 // (50)
D=D+A               // (51)
@13                 // (52)
M=D                 // (53)
@SP                 // (54)
M=M-1               // (55)
A=M                 // (56)
D=M                 // (57)
@13                 // (58)
A=M                 // (59)
M=D                 // (60)

// push argument 0
@0                  // (61)
D=A                 // (62)
@ARG                // (63)
A=M                 // (64)
A=A+D               // (65)
D=M                 // (66)
@SP                 // (67)
M=M+1               // (68)
A=M-1               // (69)
M=D                 // (70)

// push constant 1
@1                  // (71)
D=A                 // (72)
@SP                 // (73)
M=M+1               // (74)
A=M-1               // (75)
M=D                 // (76)

// sub
@SP                 // (77)
A=M-1               // (78)
D=M                 // (79)
A=A-1               // (80)
M=M-D               // (81)
@SP                 // (82)
M=M-1               // (83)

// pop argument 0
@0                  // (84)
D=A                 // (85)
@ARG                // (86)
A=M                 // (87)
D=D+A               // (88)
@13                 // (89)
M=D                 // (90)
@SP                 // (91)
M=M-1               // (92)
A=M                 // (93)
D=M                 // (94)
@13                 // (95)
A=M                 // (96)
M=D                 // (97)

// push argument 0
@0                  // (98)
D=A                 // (99)
@ARG                // (100)
A=M                 // (101)
A=A+D               // (102)
D=M                 // (103)
@SP                 // (104)
M=M+1               // (105)
A=M-1               // (106)
M=D                 // (107)

// if-goto LOOP_START
@SP                 // (108)
M=M-1               // (109)
A=M                 // (110)
D=M                 // (111)
@LOOP_START         // (112)
D;JNE               // (113)

// push local 0
@0                  // (114)
D=A                 // (115)
@LCL                // (116)
A=M                 // (117)
A=A+D               // (118)
D=M                 // (119)
@SP                 // (120)
M=M+1               // (121)
A=M-1               // (122)
M=D                 // (123)
