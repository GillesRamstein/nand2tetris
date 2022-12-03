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

// push constant 6
@6                  // (61)
D=A                 // (62)
@SP                 // (63)
M=M+1               // (64)
A=M-1               // (65)
M=D                 // (66)

// push constant 8
@8                  // (67)
D=A                 // (68)
@SP                 // (69)
M=M+1               // (70)
A=M-1               // (71)
M=D                 // (72)

// call Class1.set 2
@Class1.set.RETURN_ADDRESS  // (73)
D=A                 // (74)
@SP                 // (75)
M=M+1               // (76)
A=M-1               // (77)
M=D                 // (78)  push return_address onto stack
@LCL                // (79)
D=M                 // (80)
@SP                 // (81)
M=M+1               // (82)
A=M-1               // (83)
M=D                 // (84)  push *LCL onto stack
@ARG                // (85)
D=M                 // (86)
@SP                 // (87)
M=M+1               // (88)
A=M-1               // (89)
M=D                 // (90)  push *ARG onto stack
@THIS               // (91)
D=M                 // (92)
@SP                 // (93)
M=M+1               // (94)
A=M-1               // (95)
M=D                 // (96)  push *THIS onto stack
@THAT               // (97)
D=M                 // (98)
@SP                 // (99)
M=M+1               // (100)
A=M-1               // (101)
M=D                 // (102)  push *THAT onto stack
@SP                 // (103)
D=M                 // (104)
@LCL                // (105)
M=D                 // (106)  reposition LCL to *SP
D=D-1               // (107)
D=D-1               // (108)
D=D-1               // (109)
D=D-1               // (110)
D=D-1               // (111)
D=D-1               // (112)
D=D-1               // (113)
@ARG                // (114)
M=D                 // (115)  reposition ARG to *SP-5-2
@Class1.set         // (116)
0;JMP               // (117)

(Class1.set.RETURN_ADDRESS)

// pop temp 0
@SP                 // (118)
M=M-1               // (119)
A=M                 // (120)
D=M                 // (121)
@5                  // (122)
M=D                 // (123)

// push constant 23
@23                 // (124)
D=A                 // (125)
@SP                 // (126)
M=M+1               // (127)
A=M-1               // (128)
M=D                 // (129)

// push constant 15
@15                 // (130)
D=A                 // (131)
@SP                 // (132)
M=M+1               // (133)
A=M-1               // (134)
M=D                 // (135)

// call Class2.set 2
@Class2.set.RETURN_ADDRESS  // (136)
D=A                 // (137)
@SP                 // (138)
M=M+1               // (139)
A=M-1               // (140)
M=D                 // (141)  push return_address onto stack
@LCL                // (142)
D=M                 // (143)
@SP                 // (144)
M=M+1               // (145)
A=M-1               // (146)
M=D                 // (147)  push *LCL onto stack
@ARG                // (148)
D=M                 // (149)
@SP                 // (150)
M=M+1               // (151)
A=M-1               // (152)
M=D                 // (153)  push *ARG onto stack
@THIS               // (154)
D=M                 // (155)
@SP                 // (156)
M=M+1               // (157)
A=M-1               // (158)
M=D                 // (159)  push *THIS onto stack
@THAT               // (160)
D=M                 // (161)
@SP                 // (162)
M=M+1               // (163)
A=M-1               // (164)
M=D                 // (165)  push *THAT onto stack
@SP                 // (166)
D=M                 // (167)
@LCL                // (168)
M=D                 // (169)  reposition LCL to *SP
D=D-1               // (170)
D=D-1               // (171)
D=D-1               // (172)
D=D-1               // (173)
D=D-1               // (174)
D=D-1               // (175)
D=D-1               // (176)
@ARG                // (177)
M=D                 // (178)  reposition ARG to *SP-5-2
@Class2.set         // (179)
0;JMP               // (180)

(Class2.set.RETURN_ADDRESS)

// pop temp 0
@SP                 // (181)
M=M-1               // (182)
A=M                 // (183)
D=M                 // (184)
@5                  // (185)
M=D                 // (186)

// call Class1.get 0
@Class1.get.RETURN_ADDRESS  // (187)
D=A                 // (188)
@SP                 // (189)
M=M+1               // (190)
A=M-1               // (191)
M=D                 // (192)  push return_address onto stack
@LCL                // (193)
D=M                 // (194)
@SP                 // (195)
M=M+1               // (196)
A=M-1               // (197)
M=D                 // (198)  push *LCL onto stack
@ARG                // (199)
D=M                 // (200)
@SP                 // (201)
M=M+1               // (202)
A=M-1               // (203)
M=D                 // (204)  push *ARG onto stack
@THIS               // (205)
D=M                 // (206)
@SP                 // (207)
M=M+1               // (208)
A=M-1               // (209)
M=D                 // (210)  push *THIS onto stack
@THAT               // (211)
D=M                 // (212)
@SP                 // (213)
M=M+1               // (214)
A=M-1               // (215)
M=D                 // (216)  push *THAT onto stack
@SP                 // (217)
D=M                 // (218)
@LCL                // (219)
M=D                 // (220)  reposition LCL to *SP
D=D-1               // (221)
D=D-1               // (222)
D=D-1               // (223)
D=D-1               // (224)
D=D-1               // (225)
@ARG                // (226)
M=D                 // (227)  reposition ARG to *SP-5-0
@Class1.get         // (228)
0;JMP               // (229)

(Class1.get.RETURN_ADDRESS)

// call Class2.get 0
@Class2.get.RETURN_ADDRESS  // (230)
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
@ARG                // (269)
M=D                 // (270)  reposition ARG to *SP-5-0
@Class2.get         // (271)
0;JMP               // (272)

(Class2.get.RETURN_ADDRESS)

// label WHILE
(WHILE)

// goto WHILE
@WHILE              // (273)
0;JMP               // (274)

// function Class2.set 0
(Class2.set)

// push argument 0
@0                  // (275)
D=A                 // (276)
@ARG                // (277)
A=M                 // (278)
A=A+D               // (279)
D=M                 // (280)
@SP                 // (281)
M=M+1               // (282)
A=M-1               // (283)
M=D                 // (284)

// pop static 0
// static index: 0
@SP                 // (285)
M=M-1               // (286)
A=M                 // (287)
D=M                 // (288)
@16                 // (289)
M=D                 // (290)

// push argument 1
@1                  // (291)
D=A                 // (292)
@ARG                // (293)
A=M                 // (294)
A=A+D               // (295)
D=M                 // (296)
@SP                 // (297)
M=M+1               // (298)
A=M-1               // (299)
M=D                 // (300)

// pop static 1
// static index: 1
@SP                 // (301)
M=M-1               // (302)
A=M                 // (303)
D=M                 // (304)
@17                 // (305)
M=D                 // (306)

// push constant 0
@0                  // (307)
D=A                 // (308)
@SP                 // (309)
M=M+1               // (310)
A=M-1               // (311)
M=D                 // (312)

// return
// (from Class2.set to Sys.init)
@LCL                // (313)
A=M-1               // (314)  LCL-1
A=A-1               // (315)  LCL-2
A=A-1               // (316)  LCL-3
A=A-1               // (317)  LCL-4
A=A-1               // (318)  LCL-5
D=M                 // (319)  return_address from *LCL-5 to D
@13                 // (320)
M=D                 // (321)  store return_address in R13
@SP                 // (322)
A=M-1               // (323)
D=M                 // (324)  return_value from *SP-1 to D
@ARG                // (325)
A=M                 // (326)
M=D                 // (327)  store return_value in *ARG
D=A                 // (328)
@SP                 // (329)
M=D+1               // (330)  *SP = *ARG+1
@LCL                // (331)
M=M-1               // (332)  endFrame-1
A=M                 // (333)
D=M                 // (334)
@THAT               // (335)
M=D                 // (336)  restore THAT pointer
@LCL                // (337)
M=M-1               // (338)  endFrame-2
A=M                 // (339)
D=M                 // (340)
@THIS               // (341)
M=D                 // (342)  restore THIS pointer
@LCL                // (343)
M=M-1               // (344)  endFrame-3
A=M                 // (345)
D=M                 // (346)
@ARG                // (347)
M=D                 // (348)  restore ARG pointer
@LCL                // (349)
M=M-1               // (350)  endFrame-4
A=M                 // (351)
D=M                 // (352)
@LCL                // (353)
M=D                 // (354)  restore LCL pointer
@13                 // (355)
A=M                 // (356)  load return_address from R13
0;JMP               // (357)  jump to return_address

// function Class2.get 0
(Class2.get)

// push static 0
// static index: 0
@16                 // (358)
D=M                 // (359)
@SP                 // (360)
M=M+1               // (361)
A=M-1               // (362)
M=D                 // (363)

// push static 1
// static index: 1
@17                 // (364)
D=M                 // (365)
@SP                 // (366)
M=M+1               // (367)
A=M-1               // (368)
M=D                 // (369)

// sub
@SP                 // (370)
A=M-1               // (371)
D=M                 // (372)
A=A-1               // (373)
M=M-D               // (374)
@SP                 // (375)
M=M-1               // (376)

// return
// (from Class2.get to Sys.init)
@LCL                // (377)
A=M-1               // (378)  LCL-1
A=A-1               // (379)  LCL-2
A=A-1               // (380)  LCL-3
A=A-1               // (381)  LCL-4
A=A-1               // (382)  LCL-5
D=M                 // (383)  return_address from *LCL-5 to D
@13                 // (384)
M=D                 // (385)  store return_address in R13
@SP                 // (386)
A=M-1               // (387)
D=M                 // (388)  return_value from *SP-1 to D
@ARG                // (389)
A=M                 // (390)
M=D                 // (391)  store return_value in *ARG
D=A                 // (392)
@SP                 // (393)
M=D+1               // (394)  *SP = *ARG+1
@LCL                // (395)
M=M-1               // (396)  endFrame-1
A=M                 // (397)
D=M                 // (398)
@THAT               // (399)
M=D                 // (400)  restore THAT pointer
@LCL                // (401)
M=M-1               // (402)  endFrame-2
A=M                 // (403)
D=M                 // (404)
@THIS               // (405)
M=D                 // (406)  restore THIS pointer
@LCL                // (407)
M=M-1               // (408)  endFrame-3
A=M                 // (409)
D=M                 // (410)
@ARG                // (411)
M=D                 // (412)  restore ARG pointer
@LCL                // (413)
M=M-1               // (414)  endFrame-4
A=M                 // (415)
D=M                 // (416)
@LCL                // (417)
M=D                 // (418)  restore LCL pointer
@13                 // (419)
A=M                 // (420)  load return_address from R13
0;JMP               // (421)  jump to return_address

// function Class1.set 0
(Class1.set)

// push argument 0
@0                  // (422)
D=A                 // (423)
@ARG                // (424)
A=M                 // (425)
A=A+D               // (426)
D=M                 // (427)
@SP                 // (428)
M=M+1               // (429)
A=M-1               // (430)
M=D                 // (431)

// pop static 0
// static index: 2
@SP                 // (432)
M=M-1               // (433)
A=M                 // (434)
D=M                 // (435)
@18                 // (436)
M=D                 // (437)

// push argument 1
@1                  // (438)
D=A                 // (439)
@ARG                // (440)
A=M                 // (441)
A=A+D               // (442)
D=M                 // (443)
@SP                 // (444)
M=M+1               // (445)
A=M-1               // (446)
M=D                 // (447)

// pop static 1
// static index: 3
@SP                 // (448)
M=M-1               // (449)
A=M                 // (450)
D=M                 // (451)
@19                 // (452)
M=D                 // (453)

// push constant 0
@0                  // (454)
D=A                 // (455)
@SP                 // (456)
M=M+1               // (457)
A=M-1               // (458)
M=D                 // (459)

// return
// (from Class1.set to Sys.init)
@LCL                // (460)
A=M-1               // (461)  LCL-1
A=A-1               // (462)  LCL-2
A=A-1               // (463)  LCL-3
A=A-1               // (464)  LCL-4
A=A-1               // (465)  LCL-5
D=M                 // (466)  return_address from *LCL-5 to D
@13                 // (467)
M=D                 // (468)  store return_address in R13
@SP                 // (469)
A=M-1               // (470)
D=M                 // (471)  return_value from *SP-1 to D
@ARG                // (472)
A=M                 // (473)
M=D                 // (474)  store return_value in *ARG
D=A                 // (475)
@SP                 // (476)
M=D+1               // (477)  *SP = *ARG+1
@LCL                // (478)
M=M-1               // (479)  endFrame-1
A=M                 // (480)
D=M                 // (481)
@THAT               // (482)
M=D                 // (483)  restore THAT pointer
@LCL                // (484)
M=M-1               // (485)  endFrame-2
A=M                 // (486)
D=M                 // (487)
@THIS               // (488)
M=D                 // (489)  restore THIS pointer
@LCL                // (490)
M=M-1               // (491)  endFrame-3
A=M                 // (492)
D=M                 // (493)
@ARG                // (494)
M=D                 // (495)  restore ARG pointer
@LCL                // (496)
M=M-1               // (497)  endFrame-4
A=M                 // (498)
D=M                 // (499)
@LCL                // (500)
M=D                 // (501)  restore LCL pointer
@13                 // (502)
A=M                 // (503)  load return_address from R13
0;JMP               // (504)  jump to return_address

// function Class1.get 0
(Class1.get)

// push static 0
// static index: 2
@18                 // (505)
D=M                 // (506)
@SP                 // (507)
M=M+1               // (508)
A=M-1               // (509)
M=D                 // (510)

// push static 1
// static index: 3
@19                 // (511)
D=M                 // (512)
@SP                 // (513)
M=M+1               // (514)
A=M-1               // (515)
M=D                 // (516)

// sub
@SP                 // (517)
A=M-1               // (518)
D=M                 // (519)
A=A-1               // (520)
M=M-D               // (521)
@SP                 // (522)
M=M-1               // (523)

// return
// (from Class1.get to Sys.init)
@LCL                // (524)
A=M-1               // (525)  LCL-1
A=A-1               // (526)  LCL-2
A=A-1               // (527)  LCL-3
A=A-1               // (528)  LCL-4
A=A-1               // (529)  LCL-5
D=M                 // (530)  return_address from *LCL-5 to D
@13                 // (531)
M=D                 // (532)  store return_address in R13
@SP                 // (533)
A=M-1               // (534)
D=M                 // (535)  return_value from *SP-1 to D
@ARG                // (536)
A=M                 // (537)
M=D                 // (538)  store return_value in *ARG
D=A                 // (539)
@SP                 // (540)
M=D+1               // (541)  *SP = *ARG+1
@LCL                // (542)
M=M-1               // (543)  endFrame-1
A=M                 // (544)
D=M                 // (545)
@THAT               // (546)
M=D                 // (547)  restore THAT pointer
@LCL                // (548)
M=M-1               // (549)  endFrame-2
A=M                 // (550)
D=M                 // (551)
@THIS               // (552)
M=D                 // (553)  restore THIS pointer
@LCL                // (554)
M=M-1               // (555)  endFrame-3
A=M                 // (556)
D=M                 // (557)
@ARG                // (558)
M=D                 // (559)  restore ARG pointer
@LCL                // (560)
M=M-1               // (561)  endFrame-4
A=M                 // (562)
D=M                 // (563)
@LCL                // (564)
M=D                 // (565)  restore LCL pointer
@13                 // (566)
A=M                 // (567)  load return_address from R13
0;JMP               // (568)  jump to return_address
