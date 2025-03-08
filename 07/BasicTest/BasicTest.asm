// VM: push constant 10
// D = 10
@10
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
// VM: push constant 21
// D = 21
@21
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 22
// D = 22
@22
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop argument 2
// segment_address = ARG + 2
@2
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
// VM: pop argument 1
// segment_address = ARG + 1
@1
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
// VM: push constant 36
// D = 36
@36
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop this 6
// segment_address = THIS + 6
@6
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
// VM: push constant 42
// D = 42
@42
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 45
// D = 45
@45
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop that 5
// segment_address = THAT + 5
@5
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
// VM: push constant 510
// D = 510
@510
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop temp 6
// segment_address = 5 + 6
@6
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
// VM: push that 5
// D = data at THAT + 5
@5
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
// VM: push this 6
// D = data at THIS + 6
@6
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
// VM: push this 6
// D = data at THIS + 6
@6
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
// VM: push temp 6
// D = data at 5 + 6
@6
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