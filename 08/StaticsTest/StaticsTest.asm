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
// VM: function Class1.set 0
(Class1.set)
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
// VM: pop static 0
// pop @Class1.vm.0
// segment_address = Class1.vm.0
@Class1.vm.0
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
// VM: pop static 1
// pop @Class1.vm.1
// segment_address = Class1.vm.1
@Class1.vm.1
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
// VM: function Class1.get 0
(Class1.get)
// VM: push static 0
// push @Class1.vm.0
@Class1.vm.0
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push static 1
// push @Class1.vm.1
@Class1.vm.1
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
// VM: function Sys.init 0
(Sys.init)
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
// VM: call Class1.set 2
// push Class1.set$ret.1
@Class1.set$ret.1
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
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
// VM: goto Class1.set
@Class1.set
0;JMP
(Class1.set$ret.1)
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
// VM: push constant 23
// D = 23
@23
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 15
// D = 15
@15
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: call Class2.set 2
// push Class2.set$ret.1
@Class2.set$ret.1
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
@2
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
// VM: goto Class2.set
@Class2.set
0;JMP
(Class2.set$ret.1)
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
// VM: call Class1.get 0
// push Class1.get$ret.1
@Class1.get$ret.1
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
// VM: goto Class1.get
@Class1.get
0;JMP
(Class1.get$ret.1)
// VM: call Class2.get 0
// push Class2.get$ret.1
@Class2.get$ret.1
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
// VM: goto Class2.get
@Class2.get
0;JMP
(Class2.get$ret.1)
// VM: label END
(END)
// VM: goto END
@END
0;JMP
// VM: function Class2.set 0
(Class2.set)
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
// VM: pop static 0
// pop @Class2.vm.0
// segment_address = Class2.vm.0
@Class2.vm.0
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
// VM: pop static 1
// pop @Class2.vm.1
// segment_address = Class2.vm.1
@Class2.vm.1
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
// VM: function Class2.get 0
(Class2.get)
// VM: push static 0
// push @Class2.vm.0
@Class2.vm.0
D=M
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push static 1
// push @Class2.vm.1
@Class2.vm.1
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