// VM: push constant 7
// D = 7
@7
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 8
// D = 8
@8
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: add
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
// VM: pop temp 1
// segment_address = 5 + 1
@1
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
// execute add
@5
D=M
@6
D=D+M
@7
M=D
// VM: push temp 2
// D = data at 5 + 2
@2
D=A
@5
A=D+A
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1