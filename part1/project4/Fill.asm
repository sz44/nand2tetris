// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// keyboard @KBD
// screen @SCREEN 512 x 256
// 1 row = 32 regs
// 32 * 256 = 8192

// while true {
// 	for (i = screen; i < screen + 32 * 256; i++) {
//		if (KBD>0) 
//			SCREEN[i] = -1;
//		else
//			SCREEN[i] = 0;		
//	}
// }

// 	n = SCREEN + 32 * 256
// LOOP:
//	addr = SCREEN
// DRAW:
//	if addr == n goto LOOP	
//	if KBD>0 RAM[addr] = -1 else RAM[addr] = 0
//	addr = addr + 1
//	goto DRAW	 

@8192
D=A
@SCREEN
D=D+A
@n
M=D	// n = SCREEN + 8192

(LOOP)
@SCREEN
D=A
@addr
M=D	// addr = SCREEN

(DRAW)
@n
D=M
@addr
D=D-M
@LOOP
D;JEQ	// if n - addr == 0 goto LOOP

@KBD
D=M
@25
D;JGT	// if KBD > 0 goto 25

@addr
A=M
M=0	// RAM[addr] = 0
@28
0;JMP

@addr
A=M
M=-1	// RAM[addr] = -1

@addr
M=M+1	// addr = addr + 1

@DRAW
0;JMP

