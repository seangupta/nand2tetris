// VM: function SimpleFunction.test 2
(SimpleFunction.test)
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
// VM: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
// VM: not
@SP
A=M-1
M=!M
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
// VM: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
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
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
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