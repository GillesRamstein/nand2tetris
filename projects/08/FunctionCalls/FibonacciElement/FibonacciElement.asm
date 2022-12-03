// initalize pointers
@256                // (0)
D=A                 // (1)
@SP                 // (2)
M=D                 // (3)  SP=256
@0                  // (4)
D=A                 // (5)
@LCL                // (6)
D=D-1               // (7)
M=D                 // (8)  LCL=-1
@ARG                // (9)
D=D-1               // (10)
M=D                 // (11)  ARG=-2
@THIS               // (12)
D=D-1               // (13)
M=D                 // (14)  THIS=-3
@THAT               // (15)
D=D-1               // (16)
M=D                 // (17)  THAT=-4

// call Sys.init
@Sys.init.RETURN_ADDRESS  // (18)
D=A                 // (19)
@SP                 // (20)
M=M+1               // (21)
A=M-1               // (22)
M=D                 // (23)  push return_address onto stack
@LCL                // (24)
D=M                 // (25)
@SP                 // (26)
M=M+1               // (27)
A=M-1               // (28)
M=D                 // (29)  push *LCL onto stack
@ARG                // (30)
D=M                 // (31)
@SP                 // (32)
M=M+1               // (33)
A=M-1               // (34)
M=D                 // (35)  push *ARG onto stack
@THIS               // (36)
D=M                 // (37)
@SP                 // (38)
M=M+1               // (39)
A=M-1               // (40)
M=D                 // (41)  push *THIS onto stack
@THAT               // (42)
D=M                 // (43)
@SP                 // (44)
M=M+1               // (45)
A=M-1               // (46)
M=D                 // (47)  push *THAT onto stack
@SP                 // (48)
D=M                 // (49)
@LCL                // (50)
M=D                 // (51)  reposition LCL to *SP
D=D-1               // (52)
D=D-1               // (53)
D=D-1               // (54)
D=D-1               // (55)
D=D-1               // (56)
@ARG                // (57)
M=D                 // (58)  reposition ARG to *SP-5-0
@Sys.init           // (59)
0;JMP               // (60)

(Sys.init.RETURN_ADDRESS)

// function Sys.init 0
(Sys.init)

// push constant 4
@4                  // (61)
D=A                 // (62)
@SP                 // (63)
M=M+1               // (64)
A=M-1               // (65)
M=D                 // (66)

// call Main.fibonacci 1
@Main.fibonacci.RETURN_ADDRESS  // (67)
D=A                 // (68)
@SP                 // (69)
M=M+1               // (70)
A=M-1               // (71)
M=D                 // (72)  push return_address onto stack
@LCL                // (73)
D=M                 // (74)
@SP                 // (75)
M=M+1               // (76)
A=M-1               // (77)
M=D                 // (78)  push *LCL onto stack
@ARG                // (79)
D=M                 // (80)
@SP                 // (81)
M=M+1               // (82)
A=M-1               // (83)
M=D                 // (84)  push *ARG onto stack
@THIS               // (85)
D=M                 // (86)
@SP                 // (87)
M=M+1               // (88)
A=M-1               // (89)
M=D                 // (90)  push *THIS onto stack
@THAT               // (91)
D=M                 // (92)
@SP                 // (93)
M=M+1               // (94)
A=M-1               // (95)
M=D                 // (96)  push *THAT onto stack
@SP                 // (97)
D=M                 // (98)
@LCL                // (99)
M=D                 // (100)  reposition LCL to *SP
D=D-1               // (101)
D=D-1               // (102)
D=D-1               // (103)
D=D-1               // (104)
D=D-1               // (105)
D=D-1               // (106)
@ARG                // (107)
M=D                 // (108)  reposition ARG to *SP-5-1
@Main.fibonacci     // (109)
0;JMP               // (110)

(Main.fibonacci.RETURN_ADDRESS)

// label WHILE
(WHILE)

// goto WHILE
@WHILE              // (111)
0;JMP               // (112)

// function Main.fibonacci 0
(Main.fibonacci)

// push argument 0
@0                  // (113)
D=A                 // (114)
@ARG                // (115)
A=M                 // (116)
A=A+D               // (117)
D=M                 // (118)
@SP                 // (119)
M=M+1               // (120)
A=M-1               // (121)
M=D                 // (122)

// push constant 2
@2                  // (123)
D=A                 // (124)
@SP                 // (125)
M=M+1               // (126)
A=M-1               // (127)
M=D                 // (128)

// lt
@SP                 // (129)
A=M-1               // (130)
D=M                 // (131)
A=A-1               // (132)
D=M-D               // (133)
@TRUE.LT.0          // (134)
D;JLT               // (135)
D=0                 // (136)
@END.LT.0           // (137)
0;JMP               // (138)
(TRUE.LT.0)
D=-1                // (139)
(END.LT.0)
@SP                 // (140)
M=M-1               // (141)
A=M-1               // (142)
M=D                 // (143)

// if-goto IF_TRUE
@SP                 // (144)
M=M-1               // (145)
A=M                 // (146)
D=M                 // (147)
@IF_TRUE            // (148)
D;JNE               // (149)

// goto IF_FALSE
@IF_FALSE           // (150)
0;JMP               // (151)

// label IF_TRUE
(IF_TRUE)

// push argument 0
@0                  // (152)
D=A                 // (153)
@ARG                // (154)
A=M                 // (155)
A=A+D               // (156)
D=M                 // (157)
@SP                 // (158)
M=M+1               // (159)
A=M-1               // (160)
M=D                 // (161)

// return
// (from Main.fibonacci to Sys.init)
@LCL                // (162)
A=M-1               // (163)  LCL-1
A=A-1               // (164)  LCL-2
A=A-1               // (165)  LCL-3
A=A-1               // (166)  LCL-4
A=A-1               // (167)  LCL-5
D=M                 // (168)  return_address from *LCL-5 to D
@13                 // (169)
M=D                 // (170)  store return_address in R13
@SP                 // (171)
A=M-1               // (172)
D=M                 // (173)  return_value from *SP-1 to D
@ARG                // (174)
A=M                 // (175)
M=D                 // (176)  store return_value in *ARG
D=A                 // (177)
@SP                 // (178)
M=D+1               // (179)  *SP = *ARG+1
@LCL                // (180)
M=M-1               // (181)  endFrame-1
A=M                 // (182)
D=M                 // (183)
@THAT               // (184)
M=D                 // (185)  restore THAT pointer
@LCL                // (186)
M=M-1               // (187)  endFrame-2
A=M                 // (188)
D=M                 // (189)
@THIS               // (190)
M=D                 // (191)  restore THIS pointer
@LCL                // (192)
M=M-1               // (193)  endFrame-3
A=M                 // (194)
D=M                 // (195)
@ARG                // (196)
M=D                 // (197)  restore ARG pointer
@LCL                // (198)
M=M-1               // (199)  endFrame-4
A=M                 // (200)
D=M                 // (201)
@LCL                // (202)
M=D                 // (203)  restore LCL pointer
@13                 // (204)
A=M                 // (205)  load return_address from R13
0;JMP               // (206)  jump to return_address

// label IF_FALSE
(IF_FALSE)

// push argument 0
@0                  // (207)
D=A                 // (208)
@ARG                // (209)
A=M                 // (210)
A=A+D               // (211)
D=M                 // (212)
@SP                 // (213)
M=M+1               // (214)
A=M-1               // (215)
M=D                 // (216)

// push constant 2
@2                  // (217)
D=A                 // (218)
@SP                 // (219)
M=M+1               // (220)
A=M-1               // (221)
M=D                 // (222)

// sub
@SP                 // (223)
A=M-1               // (224)
D=M                 // (225)
A=A-1               // (226)
M=M-D               // (227)
@SP                 // (228)
M=M-1               // (229)

// call Main.fibonacci 1
@Main.fibonacci.RETURN_ADDRESS.REC2  // (230)
D=A                 // (231)
@SP                 // (232)
M=M+1               // (233)
A=M-1               // (234)
M=D                 // (235)  push return_address onto stack
@LCL                // (236)
D=M                 // (237)
@SP                 // (238)
M=M+1               // (239)
A=M-1               // (240)
M=D                 // (241)  push *LCL onto stack
@ARG                // (242)
D=M                 // (243)
@SP                 // (244)
M=M+1               // (245)
A=M-1               // (246)
M=D                 // (247)  push *ARG onto stack
@THIS               // (248)
D=M                 // (249)
@SP                 // (250)
M=M+1               // (251)
A=M-1               // (252)
M=D                 // (253)  push *THIS onto stack
@THAT               // (254)
D=M                 // (255)
@SP                 // (256)
M=M+1               // (257)
A=M-1               // (258)
M=D                 // (259)  push *THAT onto stack
@SP                 // (260)
D=M                 // (261)
@LCL                // (262)
M=D                 // (263)  reposition LCL to *SP
D=D-1               // (264)
D=D-1               // (265)
D=D-1               // (266)
D=D-1               // (267)
D=D-1               // (268)
D=D-1               // (269)
@ARG                // (270)
M=D                 // (271)  reposition ARG to *SP-5-1
@Main.fibonacci     // (272)
0;JMP               // (273)

(Main.fibonacci.RETURN_ADDRESS.REC2)

// push argument 0
@0                  // (274)
D=A                 // (275)
@ARG                // (276)
A=M                 // (277)
A=A+D               // (278)
D=M                 // (279)
@SP                 // (280)
M=M+1               // (281)
A=M-1               // (282)
M=D                 // (283)

// push constant 1
@1                  // (284)
D=A                 // (285)
@SP                 // (286)
M=M+1               // (287)
A=M-1               // (288)
M=D                 // (289)

// sub
@SP                 // (290)
A=M-1               // (291)
D=M                 // (292)
A=A-1               // (293)
M=M-D               // (294)
@SP                 // (295)
M=M-1               // (296)

// call Main.fibonacci 1
@Main.fibonacci.RETURN_ADDRESS.REC3  // (297)
D=A                 // (298)
@SP                 // (299)
M=M+1               // (300)
A=M-1               // (301)
M=D                 // (302)  push return_address onto stack
@LCL                // (303)
D=M                 // (304)
@SP                 // (305)
M=M+1               // (306)
A=M-1               // (307)
M=D                 // (308)  push *LCL onto stack
@ARG                // (309)
D=M                 // (310)
@SP                 // (311)
M=M+1               // (312)
A=M-1               // (313)
M=D                 // (314)  push *ARG onto stack
@THIS               // (315)
D=M                 // (316)
@SP                 // (317)
M=M+1               // (318)
A=M-1               // (319)
M=D                 // (320)  push *THIS onto stack
@THAT               // (321)
D=M                 // (322)
@SP                 // (323)
M=M+1               // (324)
A=M-1               // (325)
M=D                 // (326)  push *THAT onto stack
@SP                 // (327)
D=M                 // (328)
@LCL                // (329)
M=D                 // (330)  reposition LCL to *SP
D=D-1               // (331)
D=D-1               // (332)
D=D-1               // (333)
D=D-1               // (334)
D=D-1               // (335)
D=D-1               // (336)
@ARG                // (337)
M=D                 // (338)  reposition ARG to *SP-5-1
@Main.fibonacci     // (339)
0;JMP               // (340)

(Main.fibonacci.RETURN_ADDRESS.REC3)

// add
@SP                 // (341)
A=M-1               // (342)
D=M                 // (343)
A=A-1               // (344)
M=M+D               // (345)
@SP                 // (346)
M=M-1               // (347)

// return
// (from Sys.init to Sys.init)
@LCL                // (348)
A=M-1               // (349)  LCL-1
A=A-1               // (350)  LCL-2
A=A-1               // (351)  LCL-3
A=A-1               // (352)  LCL-4
A=A-1               // (353)  LCL-5
D=M                 // (354)  return_address from *LCL-5 to D
@13                 // (355)
M=D                 // (356)  store return_address in R13
@SP                 // (357)
A=M-1               // (358)
D=M                 // (359)  return_value from *SP-1 to D
@ARG                // (360)
A=M                 // (361)
M=D                 // (362)  store return_value in *ARG
D=A                 // (363)
@SP                 // (364)
M=D+1               // (365)  *SP = *ARG+1
@LCL                // (366)
M=M-1               // (367)  endFrame-1
A=M                 // (368)
D=M                 // (369)
@THAT               // (370)
M=D                 // (371)  restore THAT pointer
@LCL                // (372)
M=M-1               // (373)  endFrame-2
A=M                 // (374)
D=M                 // (375)
@THIS               // (376)
M=D                 // (377)  restore THIS pointer
@LCL                // (378)
M=M-1               // (379)  endFrame-3
A=M                 // (380)
D=M                 // (381)
@ARG                // (382)
M=D                 // (383)  restore ARG pointer
@LCL                // (384)
M=M-1               // (385)  endFrame-4
A=M                 // (386)
D=M                 // (387)
@LCL                // (388)
M=D                 // (389)  restore LCL pointer
@13                 // (390)
A=M                 // (391)  load return_address from R13
0;JMP               // (392)  jump to return_address
