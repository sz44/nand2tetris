// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

// for (i = 0; i < R0; i++) {
//	R2 = R2 + R1
// }

//      R2 = 0
// 	i = 0
// 	n = R0
// 	m = R1
// 	res = 0
// LOOP:
// 	if i == n goto END
// 	res = res + m
// 	i = i + 1
// 	goto LOOP
// STOP:
//	R2 = res 

@R2
M=0
@i
M=0	// i = 0
@R0
D=M
@n
M=D	// n = R0
@R1
D=M
@m
M=D	// m = R1
@res
M=0	// res = 0

(LOOP)
@i
D=M
@n
D=D-M
@STOP
D;JEQ	// if i == n goto STOP 

@m
D=M
@res
M=D+M 	// res = res + m

@i
M=M+1	// i = i + 1

@LOOP
0;JMP

(STOP)
@res
D=M
@R2
M=D	// R2 = res

(END)
@END
0;JMP