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
// VM: function Main.fibonacci 0
(Main.fibonacci)
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
// VM: lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@TRUE0
D;JLT
@SP
A=M-1
M=0
(TRUE0)
// VM: if-goto N_LT_2
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
@N_LT_2
D;JNE
// VM: goto N_GE_2
@N_GE_2
0;JMP
// VM: label N_LT_2
(N_LT_2)
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
// VM: label N_GE_2
(N_GE_2)
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
// VM: call Main.fibonacci 1
// push Main.fibonacci$ret.1
@Main.fibonacci$ret.1
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
// VM: goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)
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
// VM: call Main.fibonacci 1
// push Main.fibonacci$ret.2
@Main.fibonacci$ret.2
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
// VM: goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)
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
// VM: function Sys.init 0
(Sys.init)
// VM: push constant 4
// D = 4
@4
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: call Main.fibonacci 1
// push Main.fibonacci$ret.3
@Main.fibonacci$ret.3
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
// VM: goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.3)
// VM: label END
(END)
// VM: goto END
@END
0;JMP