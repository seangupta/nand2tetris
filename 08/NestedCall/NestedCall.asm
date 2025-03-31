// Bootstrap code
@256
D=A
@SP
M=D
// call Sys.init
// VM: call Sys.init 0
// push Sys.init$ret.1
@Sys.init$ret.1
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at LCL
@LCL
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at ARG
@ARG
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at THIS
@THIS
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at THAT
@THAT
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
// VM: goto Sys.init
@Sys.init
0;JMP
(Sys.init$ret.1)
// VM: function Sys.init 0
(Sys.init)
// VM: push constant 4000
// D = 4000
@4000
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
// VM: push constant 5000
// D = 5000
@5000
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
// VM: call Sys.main 0
// push Sys.main$ret.1
@Sys.main$ret.1
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at LCL
@LCL
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at ARG
@ARG
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at THIS
@THIS
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at THAT
@THAT
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
// VM: goto Sys.main
@Sys.main
0;JMP
(Sys.main$ret.1)
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
// VM: label LOOP
(LOOP)
// VM: goto LOOP
@LOOP
0;JMP
// VM: function Sys.main 5
(Sys.main)
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
// VM: push constant 4001
// D = 4001
@4001
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
// VM: push constant 5001
// D = 5001
@5001
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
// VM: push constant 200
// D = 200
@200
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop local 1
// segment_address = LCL + 1
@1
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
// VM: push constant 40
// D = 40
@40
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop local 2
// segment_address = LCL + 2
@2
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
// VM: push constant 6
// D = 6
@6
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: pop local 3
// segment_address = LCL + 3
@3
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
// VM: push constant 123
// D = 123
@123
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: call Sys.add12 1
// push Sys.add12$ret.1
@Sys.add12$ret.1
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at LCL
@LCL
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at ARG
@ARG
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at THIS
@THIS
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// push value at THAT
@THAT
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
// VM: goto Sys.add12
@Sys.add12
0;JMP
(Sys.add12$ret.1)
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
// VM: push local 1
// D = data at LCL + 1
@1
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
// VM: push local 2
// D = data at LCL + 2
@2
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
// VM: push local 3
// D = data at LCL + 3
@3
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
// VM: push local 4
// D = data at LCL + 4
@4
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
// VM: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
// VM: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
// VM: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
// VM: return
// endFrame = LCL
@LCL
D=M
@END_FRAME
M=D
// retAddr = *(endFrame - 5)
@5
D=A
@END_FRAME
A=M-D
D=M
@RET_ADDR
M=D
// *ARG = pop()
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M+1
@SP
M=D
// THAT = *(endFrame - 1)
@1
D=A
@END_FRAME
A=M-D
D=M
@THAT
M=D
// THIS = *(endFrame - 2)
@2
D=A
@END_FRAME
A=M-D
D=M
@THIS
M=D
// ARG = *(endFrame - 3)
@3
D=A
@END_FRAME
A=M-D
D=M
@ARG
M=D
// LCL = *(endFrame - 4)
@4
D=A
@END_FRAME
A=M-D
D=M
@LCL
M=D
@RET_ADDR
A=M
0;JMP
// VM: function Sys.add12 0
(Sys.add12)
// VM: push constant 4002
// D = 4002
@4002
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
// VM: push constant 5002
// D = 5002
@5002
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
// VM: push constant 12
// D = 12
@12
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
// VM: return
// endFrame = LCL
@LCL
D=M
@END_FRAME
M=D
// retAddr = *(endFrame - 5)
@5
D=A
@END_FRAME
A=M-D
D=M
@RET_ADDR
M=D
// *ARG = pop()
// SP--
@SP
M=M-1
// D = RAM[SP]
@SP
A=M
D=M
@ARG
A=M
M=D
// SP = ARG + 1
@ARG
D=M+1
@SP
M=D
// THAT = *(endFrame - 1)
@1
D=A
@END_FRAME
A=M-D
D=M
@THAT
M=D
// THIS = *(endFrame - 2)
@2
D=A
@END_FRAME
A=M-D
D=M
@THIS
M=D
// ARG = *(endFrame - 3)
@3
D=A
@END_FRAME
A=M-D
D=M
@ARG
M=D
// LCL = *(endFrame - 4)
@4
D=A
@END_FRAME
A=M-D
D=M
@LCL
M=D
@RET_ADDR
A=M
0;JMP