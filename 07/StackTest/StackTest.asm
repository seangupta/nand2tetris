// VM: push constant 17
// D = 17
@17
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 17
// D = 17
@17
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: eq
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
// execute eq
@5
D=M
@6
D=D-M
@7
M=-1
@TRUE0
D;JEQ
@7
M=0
(TRUE0)
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
// VM: push constant 17
// D = 17
@17
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 16
// D = 16
@16
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: eq
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
// execute eq
@5
D=M
@6
D=D-M
@7
M=-1
@TRUE1
D;JEQ
@7
M=0
(TRUE1)
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
// VM: push constant 16
// D = 16
@16
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 17
// D = 17
@17
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: eq
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
// execute eq
@5
D=M
@6
D=D-M
@7
M=-1
@TRUE2
D;JEQ
@7
M=0
(TRUE2)
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
// VM: push constant 892
// D = 892
@892
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 891
// D = 891
@891
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: lt
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
// execute lt
@5
D=M
@6
D=D-M
@7
M=-1
@TRUE3
D;JLT
@7
M=0
(TRUE3)
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
// VM: push constant 891
// D = 891
@891
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 892
// D = 892
@892
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: lt
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
// execute lt
@5
D=M
@6
D=D-M
@7
M=-1
@TRUE4
D;JLT
@7
M=0
(TRUE4)
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
// VM: push constant 891
// D = 891
@891
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 891
// D = 891
@891
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: lt
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
// execute lt
@5
D=M
@6
D=D-M
@7
M=-1
@TRUE5
D;JLT
@7
M=0
(TRUE5)
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
// VM: push constant 32767
// D = 32767
@32767
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 32766
// D = 32766
@32766
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: gt
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
// execute gt
@5
D=M
@6
D=D-M
@7
M=-1
@TRUE6
D;JGT
@7
M=0
(TRUE6)
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
// VM: push constant 32766
// D = 32766
@32766
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 32767
// D = 32767
@32767
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: gt
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
// execute gt
@5
D=M
@6
D=D-M
@7
M=-1
@TRUE7
D;JGT
@7
M=0
(TRUE7)
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
// VM: push constant 32766
// D = 32766
@32766
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 32766
// D = 32766
@32766
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: gt
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
// execute gt
@5
D=M
@6
D=D-M
@7
M=-1
@TRUE8
D;JGT
@7
M=0
(TRUE8)
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
// VM: push constant 57
// D = 57
@57
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 31
// D = 31
@31
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: push constant 53
// D = 53
@53
D=A
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
// VM: push constant 112
// D = 112
@112
D=A
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
// VM: neg
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
// actually neg
@5
M=-M
// VM: push temp 0
// D = data at 5 + 0
@0
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
// VM: and
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
// execute and
@5
D=M
@6
D=D&M
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
// VM: push constant 82
// D = 82
@82
D=A
// RAM[SP] = D
@SP
A=M
M=D
// SP++
@SP
M=M+1
// VM: or
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
// execute or
@5
D=M
@6
D=D|M
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
// VM: not
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
// actually not
@5
M=!M
// VM: push temp 0
// D = data at 5 + 0
@0
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