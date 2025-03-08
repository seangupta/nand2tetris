// VM: push constant 111
// D = 111
@111
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 333
// D = 333
@333
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 888
// D = 888
@888
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop static 8
// pop @StaticTest.8
// segment_address = StaticTest.8
@StaticTest.8
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
// VM: pop static 3
// pop @StaticTest.3
// segment_address = StaticTest.3
@StaticTest.3
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
// VM: pop static 1
// pop @StaticTest.1
// segment_address = StaticTest.1
@StaticTest.1
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
// VM: push static 3
// push @StaticTest.3
@StaticTest.3
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push static 1
// push @StaticTest.1
@StaticTest.1
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: sub
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
// execute sub
@5
D=M
@6
D=D-M
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
// VM: push static 8
// push @StaticTest.8
@StaticTest.8
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: add
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