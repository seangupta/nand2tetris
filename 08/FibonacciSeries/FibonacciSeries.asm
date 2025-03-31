// VM: push argument 1
// D = data at ARG + 1
@1
D=A
@ARG
A=D+M
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop pointer 1
// pop THAT
// segment_address = THAT
@THAT
D=A
@segment_address
M=D
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
// RAM[segment_address] = D
@segment_address
A=M
M=D
// VM: push constant 0
// D = 0
@0
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop that 0
// segment_address = THAT + 0
@0
D=A
@THAT
D=D+M
@segment_address
M=D
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
// RAM[segment_address] = D
@segment_address
A=M
M=D
// VM: push constant 1
// D = 1
@1
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop that 1
// segment_address = THAT + 1
@1
D=A
@THAT
D=D+M
@segment_address
M=D
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
// RAM[segment_address] = D
@segment_address
A=M
M=D
// VM: push argument 0
// D = data at ARG + 0
@0
D=A
@ARG
A=D+M
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 2
// D = 2
@2
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
// VM: pop argument 0
// segment_address = ARG + 0
@0
D=A
@ARG
D=D+M
@segment_address
M=D
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
// RAM[segment_address] = D
@segment_address
A=M
M=D
// VM: label LOOP
(LOOP)
// VM: push argument 0
// D = data at ARG + 0
@0
D=A
@ARG
A=D+M
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: if-goto COMPUTE_ELEMENT
// VM: pop temp 0
// segment_address = 5 + 0
@0
D=A
@5
D=D+A
@segment_address
M=D
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
// RAM[segment_address] = D
@segment_address
A=M
M=D
@5
D=M
@COMPUTE_ELEMENT
D;JNE
// VM: goto END
@END
0;JMP
// VM: label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)
// VM: push that 0
// D = data at THAT + 0
@0
D=A
@THAT
A=D+M
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push that 1
// D = data at THAT + 1
@1
D=A
@THAT
A=D+M
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
// VM: pop that 2
// segment_address = THAT + 2
@2
D=A
@THAT
D=D+M
@segment_address
M=D
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
// RAM[segment_address] = D
@segment_address
A=M
M=D
// VM: push pointer 1
// push THAT
@THAT
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 1
// D = 1
@1
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
// VM: pop pointer 1
// pop THAT
// segment_address = THAT
@THAT
D=A
@segment_address
M=D
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
// RAM[segment_address] = D
@segment_address
A=M
M=D
// VM: push argument 0
// D = data at ARG + 0
@0
D=A
@ARG
A=D+M
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 1
// D = 1
@1
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
// VM: pop argument 0
// segment_address = ARG + 0
@0
D=A
@ARG
D=D+M
@segment_address
M=D
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
// RAM[segment_address] = D
@segment_address
A=M
M=D
// VM: goto LOOP
@LOOP
0;JMP
// VM: label END
(END)