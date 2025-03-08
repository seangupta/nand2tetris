// VM: push constant 3030
// D = 3030
@3030
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop pointer 0
// pop THIS
// segment_address = THIS
@THIS
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
// VM: push constant 3040
// D = 3040
@3040
D=A
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
// VM: push constant 32
// D = 32
@32
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop this 2
// segment_address = THIS + 2
@2
D=A
@THIS
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
// VM: push constant 46
// D = 46
@46
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop that 6
// segment_address = THAT + 6
@6
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
// VM: push pointer 0
// push THIS
@THIS
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
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
// VM: push this 2
// D = data at THIS + 2
@2
D=A
@THIS
A=D+M
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
// VM: push that 6
// D = data at THAT + 6
@6
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