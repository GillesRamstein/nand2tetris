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

// push constant 4000
@4000               // (61)
D=A                 // (62)
@SP                 // (63)
M=M+1               // (64)
A=M-1               // (65)
M=D                 // (66)

// pop pointer 0
@SP                 // (67)
M=M-1               // (68)
A=M                 // (69)
D=M                 // (70)
@3                  // (71)
M=D                 // (72)

// push constant 5000
@5000               // (73)
D=A                 // (74)
@SP                 // (75)
M=M+1               // (76)
A=M-1               // (77)
M=D                 // (78)

// pop pointer 1
@SP                 // (79)
M=M-1               // (80)
A=M                 // (81)
D=M                 // (82)
@4                  // (83)
M=D                 // (84)

// call Sys.main 0
@Sys.main.RETURN_ADDRESS  // (85)
D=A                 // (86)
@SP                 // (87)
M=M+1               // (88)
A=M-1               // (89)
M=D                 // (90)  push return_address onto stack
@LCL                // (91)
D=M                 // (92)
@SP                 // (93)
M=M+1               // (94)
A=M-1               // (95)
M=D                 // (96)  push *LCL onto stack
@ARG                // (97)
D=M                 // (98)
@SP                 // (99)
M=M+1               // (100)
A=M-1               // (101)
M=D                 // (102)  push *ARG onto stack
@THIS               // (103)
D=M                 // (104)
@SP                 // (105)
M=M+1               // (106)
A=M-1               // (107)
M=D                 // (108)  push *THIS onto stack
@THAT               // (109)
D=M                 // (110)
@SP                 // (111)
M=M+1               // (112)
A=M-1               // (113)
M=D                 // (114)  push *THAT onto stack
@SP                 // (115)
D=M                 // (116)
@LCL                // (117)
M=D                 // (118)  reposition LCL to *SP
D=D-1               // (119)
D=D-1               // (120)
D=D-1               // (121)
D=D-1               // (122)
D=D-1               // (123)
@ARG                // (124)
M=D                 // (125)  reposition ARG to *SP-5-0
@Sys.main           // (126)
0;JMP               // (127)

(Sys.main.RETURN_ADDRESS)

// pop temp 1
@SP                 // (128)
M=M-1               // (129)
A=M                 // (130)
D=M                 // (131)
@6                  // (132)
M=D                 // (133)

// label LOOP
(LOOP)

// goto LOOP
@LOOP               // (134)
0;JMP               // (135)

// function Sys.main 5
(Sys.main)
@LCL                // (136)  init local variables
A=M                 // (137)
M=0                 // (138)  init 1/5 local vars to 0
A=A+1               // (139)
M=0                 // (140)  init 2/5 local vars to 0
A=A+1               // (141)
M=0                 // (142)  init 3/5 local vars to 0
A=A+1               // (143)
M=0                 // (144)  init 4/5 local vars to 0
A=A+1               // (145)
M=0                 // (146)  init 5/5 local vars to 0
@SP                 // (147)  inc SP by 5 local vars
M=M+1               // (148)
M=M+1               // (149)
M=M+1               // (150)
M=M+1               // (151)
M=M+1               // (152)

// push constant 4001
@4001               // (153)
D=A                 // (154)
@SP                 // (155)
M=M+1               // (156)
A=M-1               // (157)
M=D                 // (158)

// pop pointer 0
@SP                 // (159)
M=M-1               // (160)
A=M                 // (161)
D=M                 // (162)
@3                  // (163)
M=D                 // (164)

// push constant 5001
@5001               // (165)
D=A                 // (166)
@SP                 // (167)
M=M+1               // (168)
A=M-1               // (169)
M=D                 // (170)

// pop pointer 1
@SP                 // (171)
M=M-1               // (172)
A=M                 // (173)
D=M                 // (174)
@4                  // (175)
M=D                 // (176)

// push constant 200
@200                // (177)
D=A                 // (178)
@SP                 // (179)
M=M+1               // (180)
A=M-1               // (181)
M=D                 // (182)

// pop local 1
@1                  // (183)
D=A                 // (184)
@LCL                // (185)
A=M                 // (186)
D=D+A               // (187)
@13                 // (188)
M=D                 // (189)
@SP                 // (190)
M=M-1               // (191)
A=M                 // (192)
D=M                 // (193)
@13                 // (194)
A=M                 // (195)
M=D                 // (196)

// push constant 40
@40                 // (197)
D=A                 // (198)
@SP                 // (199)
M=M+1               // (200)
A=M-1               // (201)
M=D                 // (202)

// pop local 2
@2                  // (203)
D=A                 // (204)
@LCL                // (205)
A=M                 // (206)
D=D+A               // (207)
@13                 // (208)
M=D                 // (209)
@SP                 // (210)
M=M-1               // (211)
A=M                 // (212)
D=M                 // (213)
@13                 // (214)
A=M                 // (215)
M=D                 // (216)

// push constant 6
@6                  // (217)
D=A                 // (218)
@SP                 // (219)
M=M+1               // (220)
A=M-1               // (221)
M=D                 // (222)

// pop local 3
@3                  // (223)
D=A                 // (224)
@LCL                // (225)
A=M                 // (226)
D=D+A               // (227)
@13                 // (228)
M=D                 // (229)
@SP                 // (230)
M=M-1               // (231)
A=M                 // (232)
D=M                 // (233)
@13                 // (234)
A=M                 // (235)
M=D                 // (236)

// push constant 123
@123                // (237)
D=A                 // (238)
@SP                 // (239)
M=M+1               // (240)
A=M-1               // (241)
M=D                 // (242)

// call Sys.add12 1
@Sys.add12.RETURN_ADDRESS  // (243)
D=A                 // (244)
@SP                 // (245)
M=M+1               // (246)
A=M-1               // (247)
M=D                 // (248)  push return_address onto stack
@LCL                // (249)
D=M                 // (250)
@SP                 // (251)
M=M+1               // (252)
A=M-1               // (253)
M=D                 // (254)  push *LCL onto stack
@ARG                // (255)
D=M                 // (256)
@SP                 // (257)
M=M+1               // (258)
A=M-1               // (259)
M=D                 // (260)  push *ARG onto stack
@THIS               // (261)
D=M                 // (262)
@SP                 // (263)
M=M+1               // (264)
A=M-1               // (265)
M=D                 // (266)  push *THIS onto stack
@THAT               // (267)
D=M                 // (268)
@SP                 // (269)
M=M+1               // (270)
A=M-1               // (271)
M=D                 // (272)  push *THAT onto stack
@SP                 // (273)
D=M                 // (274)
@LCL                // (275)
M=D                 // (276)  reposition LCL to *SP
D=D-1               // (277)
D=D-1               // (278)
D=D-1               // (279)
D=D-1               // (280)
D=D-1               // (281)
D=D-1               // (282)
@ARG                // (283)
M=D                 // (284)  reposition ARG to *SP-5-1
@Sys.add12          // (285)
0;JMP               // (286)

(Sys.add12.RETURN_ADDRESS)

// pop temp 0
@SP                 // (287)
M=M-1               // (288)
A=M                 // (289)
D=M                 // (290)
@5                  // (291)
M=D                 // (292)

// push local 0
@0                  // (293)
D=A                 // (294)
@LCL                // (295)
A=M                 // (296)
A=A+D               // (297)
D=M                 // (298)
@SP                 // (299)
M=M+1               // (300)
A=M-1               // (301)
M=D                 // (302)

// push local 1
@1                  // (303)
D=A                 // (304)
@LCL                // (305)
A=M                 // (306)
A=A+D               // (307)
D=M                 // (308)
@SP                 // (309)
M=M+1               // (310)
A=M-1               // (311)
M=D                 // (312)

// push local 2
@2                  // (313)
D=A                 // (314)
@LCL                // (315)
A=M                 // (316)
A=A+D               // (317)
D=M                 // (318)
@SP                 // (319)
M=M+1               // (320)
A=M-1               // (321)
M=D                 // (322)

// push local 3
@3                  // (323)
D=A                 // (324)
@LCL                // (325)
A=M                 // (326)
A=A+D               // (327)
D=M                 // (328)
@SP                 // (329)
M=M+1               // (330)
A=M-1               // (331)
M=D                 // (332)

// push local 4
@4                  // (333)
D=A                 // (334)
@LCL                // (335)
A=M                 // (336)
A=A+D               // (337)
D=M                 // (338)
@SP                 // (339)
M=M+1               // (340)
A=M-1               // (341)
M=D                 // (342)

// add
@SP                 // (343)
A=M-1               // (344)
D=M                 // (345)
A=A-1               // (346)
M=M+D               // (347)
@SP                 // (348)
M=M-1               // (349)

// add
@SP                 // (350)
A=M-1               // (351)
D=M                 // (352)
A=A-1               // (353)
M=M+D               // (354)
@SP                 // (355)
M=M-1               // (356)

// add
@SP                 // (357)
A=M-1               // (358)
D=M                 // (359)
A=A-1               // (360)
M=M+D               // (361)
@SP                 // (362)
M=M-1               // (363)

// add
@SP                 // (364)
A=M-1               // (365)
D=M                 // (366)
A=A-1               // (367)
M=M+D               // (368)
@SP                 // (369)
M=M-1               // (370)

// return
// (from Sys.main to Sys.init)
@LCL                // (371)
A=M-1               // (372)  LCL-1
A=A-1               // (373)  LCL-2
A=A-1               // (374)  LCL-3
A=A-1               // (375)  LCL-4
A=A-1               // (376)  LCL-5
D=M                 // (377)  return_address from *LCL-5 to D
@13                 // (378)
M=D                 // (379)  store return_address in R13
@SP                 // (380)
A=M-1               // (381)
D=M                 // (382)  return_value from *SP-1 to D
@ARG                // (383)
A=M                 // (384)
M=D                 // (385)  store return_value in *ARG
D=A                 // (386)
@SP                 // (387)
M=D+1               // (388)  *SP = *ARG+1
@LCL                // (389)
M=M-1               // (390)  endFrame-1
A=M                 // (391)
D=M                 // (392)
@THAT               // (393)
M=D                 // (394)  restore THAT pointer
@LCL                // (395)
M=M-1               // (396)  endFrame-2
A=M                 // (397)
D=M                 // (398)
@THIS               // (399)
M=D                 // (400)  restore THIS pointer
@LCL                // (401)
M=M-1               // (402)  endFrame-3
A=M                 // (403)
D=M                 // (404)
@ARG                // (405)
M=D                 // (406)  restore ARG pointer
@LCL                // (407)
M=M-1               // (408)  endFrame-4
A=M                 // (409)
D=M                 // (410)
@LCL                // (411)
M=D                 // (412)  restore LCL pointer
@13                 // (413)
A=M                 // (414)  load return_address from R13
0;JMP               // (415)  jump to return_address

// function Sys.add12 0
(Sys.add12)

// push constant 4002
@4002               // (416)
D=A                 // (417)
@SP                 // (418)
M=M+1               // (419)
A=M-1               // (420)
M=D                 // (421)

// pop pointer 0
@SP                 // (422)
M=M-1               // (423)
A=M                 // (424)
D=M                 // (425)
@3                  // (426)
M=D                 // (427)

// push constant 5002
@5002               // (428)
D=A                 // (429)
@SP                 // (430)
M=M+1               // (431)
A=M-1               // (432)
M=D                 // (433)

// pop pointer 1
@SP                 // (434)
M=M-1               // (435)
A=M                 // (436)
D=M                 // (437)
@4                  // (438)
M=D                 // (439)

// push argument 0
@0                  // (440)
D=A                 // (441)
@ARG                // (442)
A=M                 // (443)
A=A+D               // (444)
D=M                 // (445)
@SP                 // (446)
M=M+1               // (447)
A=M-1               // (448)
M=D                 // (449)

// push constant 12
@12                 // (450)
D=A                 // (451)
@SP                 // (452)
M=M+1               // (453)
A=M-1               // (454)
M=D                 // (455)

// add
@SP                 // (456)
A=M-1               // (457)
D=M                 // (458)
A=A-1               // (459)
M=M+D               // (460)
@SP                 // (461)
M=M-1               // (462)

// return
// (from Sys.add12 to Sys.init)
@LCL                // (463)
A=M-1               // (464)  LCL-1
A=A-1               // (465)  LCL-2
A=A-1               // (466)  LCL-3
A=A-1               // (467)  LCL-4
A=A-1               // (468)  LCL-5
D=M                 // (469)  return_address from *LCL-5 to D
@13                 // (470)
M=D                 // (471)  store return_address in R13
@SP                 // (472)
A=M-1               // (473)
D=M                 // (474)  return_value from *SP-1 to D
@ARG                // (475)
A=M                 // (476)
M=D                 // (477)  store return_value in *ARG
D=A                 // (478)
@SP                 // (479)
M=D+1               // (480)  *SP = *ARG+1
@LCL                // (481)
M=M-1               // (482)  endFrame-1
A=M                 // (483)
D=M                 // (484)
@THAT               // (485)
M=D                 // (486)  restore THAT pointer
@LCL                // (487)
M=M-1               // (488)  endFrame-2
A=M                 // (489)
D=M                 // (490)
@THIS               // (491)
M=D                 // (492)  restore THIS pointer
@LCL                // (493)
M=M-1               // (494)  endFrame-3
A=M                 // (495)
D=M                 // (496)
@ARG                // (497)
M=D                 // (498)  restore ARG pointer
@LCL                // (499)
M=M-1               // (500)  endFrame-4
A=M                 // (501)
D=M                 // (502)
@LCL                // (503)
M=D                 // (504)  restore LCL pointer
@13                 // (505)
A=M                 // (506)  load return_address from R13
0;JMP               // (507)  jump to return_address
