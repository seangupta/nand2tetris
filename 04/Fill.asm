// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.

(LOOP)
@KBD
D=M // get char code of currently pressed key

@PRESSED_KEY
D;JNE // determine if key pressed

(NO_PRESSED_KEY)
@color
M=0 // white

@COLOUR_SCREEN
0;JMP

(PRESSED_KEY)
@color
M=-1 // black

(COLOUR_SCREEN)
@row
M=0 // initialise row = 0

(ROW_LOOP)
@8191
D=A

@row
D=D-M

@LOOP
D;JLT // jump back to outer loop if all memory map rows processed (row > 8191)

@SCREEN
D=A

@row
D=D+M // add row to screen idx

@abs_idx
M=D // address we actually need to access

@color
D=M // get stored color

@abs_idx
A=M // get stored address
M=D // set row color to stored color

@row
M=M+1 // row = row + 1

@ROW_LOOP
0;JMP

@LOOP
0;JMP

