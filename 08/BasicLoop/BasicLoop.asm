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
// VM: pop local 0
// segment_address = LCL + 0
@0
D=A
@LCL
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
// VM: push local 0
// D = data at LCL + 0
@0
D=A
@LCL
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
// VM: pop local 0
// segment_address = LCL + 0
@0
D=A
@LCL
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
// VM: if-goto LOOP
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
@LOOP
D;JNE
// VM: push local 0
// D = data at LCL + 0
@0
D=A
@LCL
A=D+M
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1