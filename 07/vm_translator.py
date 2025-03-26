import argparse
import os

CONSTANT = "constant"
LOCAL = "local"
ARGUMENT = "argument"
THIS = "this"
THAT = "that"
TEMP = "temp"
POINTER = "pointer"
STATIC = "static"

SP = "SP"
LCL = "LCL"
ARG = "ARG"
THIS_SYMBOL = "THIS"
THAT_SYMBOL = "THAT"

END_FRAME = "END_FRAME"
RET_ADDR = "RET_ADDR"

ADD = "add"
SUB = "sub"
NEG = "neg"
EQ = "eq"
GT = "gt"
LT = "lt"
AND = "and"
OR = "or"
NOT = "not"

BINARY_OPS = [ADD, SUB, EQ, GT, LT, AND, OR]
UNARY_OPS = [NEG, NOT]

SEGMENT_TO_BASE_ADDRESS = {
    LOCAL: LCL,
    ARGUMENT: ARG,
    THIS: THIS_SYMBOL,
    THAT: THAT_SYMBOL,
}

POINTER_LOCATION_TO_SYMBOL = {
    0: THIS_SYMBOL,
    1: THAT_SYMBOL,
}

class VmTranslator():

    def __init__(self, fn):
        self.num_labels = 0
        self.fn = fn
        self.call_counters = {}

    @staticmethod
    def pre_process(lines):
        print("Stripping whitespace and comments")
        lines_stripped = []
        for line in lines:
            line = line.split("//")[0]
            line = line.strip()
            if line:
                print(line)
                lines_stripped.append(line)

        return lines_stripped
    
    def generate_bootstrap_code(self):
        new_lines = [
            "// Bootstrap code",
            "@256",
            "D=A",
            "@SP",
            "M=D",
            "// call Sys.init",
        ]

        nl = self.translate_call("Sys.init", 0)
        new_lines.extend(nl)
        
        return new_lines

    def process(self, lines_stripped):     
        processed_lines = []

        # new_lines = self.generate_bootstrap_code()
        # processed_lines.extend(new_lines)

        for line in lines_stripped:

            line_parts = line.split()
            first_part = line_parts[0]
            if first_part == "push":
                assert len(line_parts) == 3
                segment = line_parts[1]
                i = int(line_parts[2])
                assert i >= 0
                new_lines = self.translate_push(segment, i)
            elif first_part == "pop":
                assert len(line_parts) == 3
                segment = line_parts[1]
                i = int(line_parts[2])
                assert i >= 0
                new_lines = self.translate_pop(segment, i)
            elif first_part in BINARY_OPS:
                assert len(line_parts) == 1
                new_lines = self.translate_binary_op(first_part)
            elif first_part in UNARY_OPS:
                assert len(line_parts) == 1
                new_lines = self.translate_unary_op(first_part)
            elif first_part == "label":
                assert len(line_parts) == 2
                label = line_parts[1]
                new_lines = self.translate_label(label)
            elif first_part == "goto":
                assert len(line_parts) == 2
                label = line_parts[1]
                new_lines = self.translate_goto(label)
            elif first_part == "if-goto":
                assert len(line_parts) == 2
                label = line_parts[1]
                new_lines = self.translate_if_goto(label)
            elif first_part == "call":
                assert len(line_parts) == 3
                function_name = line_parts[1]
                num_args = int(line_parts[2])
                new_lines = self.translate_call(function_name, num_args)
            elif first_part == "function":
                assert len(line_parts) == 3
                function_name = line_parts[1]
                num_local_vars = int(line_parts[2])
                new_lines = self.translate_function(function_name, num_local_vars)
            elif first_part == "return":
                assert len(line_parts) == 1
                new_lines = self.translate_return()
            else:
                raise ValueError(f"Unknown first line part {first_part}")

            processed_lines.extend(new_lines)

        return processed_lines

    def translate_push(self, segment, i):
        new_lines = [f"// VM: push {segment} {i}"]

        if segment == CONSTANT:
            nl = [
                f"// D = {i}",
                f"@{i}",
                "D=A",
                ]
        elif segment in [LOCAL, ARGUMENT, THIS, THAT]:
            segment_base_address = SEGMENT_TO_BASE_ADDRESS[segment]
            nl = [
                f"// D = data at {segment_base_address} + {i}",
                f"@{i}",
                "D=A",
                f"@{segment_base_address}",
                "A=D+M",
                "D=M",
            ]
        elif segment == TEMP:
            nl = [
                f"// D = data at 5 + {i}",
                f"@{i}",
                "D=A",
                "@5",
                "A=D+A",
                "D=M",
            ]
        elif segment == POINTER:
            assert i in POINTER_LOCATION_TO_SYMBOL
            sg = POINTER_LOCATION_TO_SYMBOL[i]
            nl = [
                f"// push {sg}",
                f"@{sg}",
                "D=M",
            ]
        elif segment == STATIC:
            var_name = f"{self.fn}.{i}"
            nl = [
                f"// push @{var_name}",
                f"@{var_name}",
                "D=M",
            ]
        else:
            raise ValueError(f"Unknown segment {segment}")
        
        new_lines.extend(nl)

        new_lines.extend(
            [
                f"// RAM[{SP}] = D",
                f"@{SP}",
                "A=M",
                "M=D",
                f"// {SP}++",
                f"@{SP}",
                "M=M+1",
                ]
        )

        return new_lines
    
    def translate_pop(self, segment, i):
        new_lines = [f"// VM: pop {segment} {i}"]

        if segment in [LOCAL, ARGUMENT, THIS, THAT]:
            segment_base_address = SEGMENT_TO_BASE_ADDRESS[segment]
            nl = [
                f"// segment_address = {segment_base_address} + {i}",
                f"@{i}",
                "D=A",
                f"@{segment_base_address}",
                "D=D+M",
                "@segment_address",
                "M=D",
            ]
        elif segment == TEMP:
            nl = [
                f"// segment_address = 5 + {i}",
                f"@{i}",
                "D=A",
                "@5",
                "D=D+A",
                "@segment_address",
                "M=D",
            ]
        elif segment == POINTER:
            assert i in POINTER_LOCATION_TO_SYMBOL
            sg = POINTER_LOCATION_TO_SYMBOL[i]
            nl = [
                f"// pop {sg}",
                f"// segment_address = {sg}",
                f"@{sg}",
                "D=A",
                "@segment_address",
                "M=D",
            ]
        elif segment == STATIC:
            var_name = f"{self.fn}.{i}"
            nl = [
                f"// pop @{var_name}",
                f"// segment_address = {var_name}",
                f"@{var_name}",
                "D=A",
                "@segment_address",
                "M=D",
            ]

        elif segment == CONSTANT:
            raise ValueError(f"Cannot pop segment {CONSTANT}")
        else:
            raise ValueError(f"Unknown segment {segment}")

        new_lines.extend(nl)

        new_lines.extend(
            [
                f"// {SP}--",
                f"@{SP}",
                "M=M-1",
                f"// D = RAM[{SP}]",
                f"@{SP}",
                "A=M",
                "D=M",
                "// RAM[segment_address] = D",
                "@segment_address",
                "A=M",
                "M=D",
            ]
        )

        return new_lines

    def translate_binary_op(self, op):
        new_lines = [f"// VM: {op}"]

        nl = self.translate_pop(TEMP, 1)
        new_lines.extend(nl)
        
        nl = self.translate_pop(TEMP, 0)
        new_lines.extend(nl)

        nl = [
            f"// execute {op}",
            "@5",
            "D=M",
            "@6",
        ]
        new_lines.extend(nl)

        if op in [ADD, SUB, AND, OR]:
            if op == ADD:
                first_line_op = "+"
            elif op == SUB:
                first_line_op = "-"
            elif op == AND:
                first_line_op = "&"
            elif op == OR:
                first_line_op = "|"

            nl = [
                f"D=D{first_line_op}M",
                "@7",
                "M=D",
                ]
            
        elif op in [EQ, GT, LT, AND, OR]:
            if op == EQ:
                first_line_op = "-"
                comp = "JEQ"
            elif op == GT:
                first_line_op = "-"
                comp = "JGT"
            elif op == LT:
                first_line_op = "-"
                comp = "JLT"
            elif op == AND:
                first_line_op = "&"
                comp = "JNE"
            elif op == OR:
                first_line_op = "|"
                comp = "JNE"

            nl = [
                f"D=D{first_line_op}M",
                "@7",
                "M=-1",
                f"@TRUE{self.num_labels}",
                f"D;{comp}",
                "@7",
                "M=0",
                f"(TRUE{self.num_labels})",
            ]
            self.num_labels += 1

        else:
            raise ValueError(f"Unknown op {op}")

        new_lines.extend(nl)

        nl = self.translate_push(TEMP, 2)
        new_lines.extend(nl)

        return new_lines

    def translate_unary_op(self, op):
        new_lines = [f"// VM: {op}"]

        nl = self.translate_pop(TEMP, 0)
        new_lines.extend(nl)

        nl = [
            f"// actually {op}",
            "@5",
        ]
        new_lines.extend(nl)

        if op == NEG:
            nl = ["M=-M"]
        elif op == NOT:
            nl = ["M=!M"]
        else:
            raise ValueError(f"Unknown op {op}")
        
        new_lines.extend(nl)

        nl = self.translate_push(TEMP, 0)
        new_lines.extend(nl)

        return new_lines
    
    @staticmethod
    def translate_label(label):
        new_lines = [
            f"// VM: label {label}",
            f"({label})"
            ]
        return new_lines
    
    @staticmethod
    def translate_goto(label):
        new_lines = [
            f"// VM: goto {label}",
            f"@{label}",
            "0;JMP",
        ]
        return new_lines
    
    def translate_if_goto(self, label):
        new_lines = [
            f"// VM: if-goto {label}",
        ]

        nl = self.translate_pop(TEMP, 0)
        new_lines.extend(nl)

        nl = [
            "@5",
            "D=M",
            f"@{label}",
            "D;JNE",
        ]
        new_lines.extend(nl)

        return new_lines
    
    @staticmethod
    def translate_push_value_at_symbol(symbol):
        assert symbol in [SP, LCL, ARG, THIS_SYMBOL, THAT_SYMBOL] or "$ret." in symbol

        new_lines = [
            f"// push value at {symbol}",
            f"@{symbol}",
            "D=M",
            f"// RAM[{SP}] = D",
            f"@{SP}",
            "A=M",
            "M=D",
            f"// {SP}++",
            f"@{SP}",
            "M=M+1",
        ]
        return new_lines

    def translate_call(self, function_name, num_args):

        new_lines = []

        call_num = self.call_counters.get(function_name, 0) + 1
        self.call_counters[function_name] = call_num

        ret_address_label = f"{function_name}$ret.{call_num}"

        nl = self.translate_push_value_at_symbol(ret_address_label)
        new_lines.extend(nl)

        ## push LCL
        nl = self.translate_push_value_at_symbol(LCL)
        new_lines.extend(nl)

        ## push ARG
        nl = self.translate_push_value_at_symbol(ARG)
        new_lines.extend(nl)

        ## push THIS
        nl = self.translate_push_value_at_symbol(THIS_SYMBOL)
        new_lines.extend(nl)

        # push THAT
        nl = self.translate_push_value_at_symbol(THAT_SYMBOL)
        new_lines.extend(nl)

        ## ARG = SP – 5 – nArgs
        nl = self.translate_push_value_at_symbol(SP)
        new_lines.extend(nl)
        nl = self.translate_push(CONSTANT, 5)
        new_lines.extend(nl)
        nl = self.translate_binary_op(SUB)
        new_lines.extend(nl)
        nl = self.translate_push(CONSTANT, num_args)
        new_lines.extend(nl)
        nl = self.translate_binary_op(SUB)
        new_lines.extend(nl)

        ## LCL = SP
        nl = [
            f"@{SP}",
            "D=M",
            f"@{LCL}",
            "M=D",
        ]
        new_lines.extend(nl)

        ## goto functionName
        nl = self.translate_goto(function_name)
        new_lines.extend(nl)

        ## (retAddrLabel)
        nl = [f"({ret_address_label})"]
        new_lines.extend(nl)
        

        return new_lines
    
    def translate_function(self, function_name, num_local_vars):
        new_lines = [
            f"// VM: function {function_name} {num_local_vars}",
            f"({function_name})",
        ]
        for _ in range(num_local_vars):
            nl = self.translate_push(CONSTANT, 0)
            new_lines.extend(nl)

        return new_lines
    
    def translate_return(self):

        new_lines = []

        ## endFrame = LCL

        nl = [
            f"// endFrame = {LCL}",
            f"@{LCL}",
            "D=M",
            f"@{END_FRAME}",
            "M=D",
            ]
        new_lines.extend(nl)

        ## retAddr = *(endFrame - 5)

        nl = ["// retAddr = *(endFrame - 5)"]
        new_lines.extend(nl)

        nl = self.translate_derefer_endframe_diff(5)
        new_lines.extend(nl)

        nl = [
            f"@{RET_ADDR}",
            "M=D",
        ]
        new_lines.extend(nl)

        ## *ARG = pop()

        nl = [
            f"// *{ARG} = pop()",
            f"// {SP}--",
            f"@{SP}",
            "M=M-1",
            f"// D = RAM[{SP}]",
            f"@{SP}",
            "A=M",
            "D=M",
            f"@{ARG}",
            "A=M",
            "M=D",
        ]
        new_lines.extend(nl)

        nl = [
            f"// {SP} = {ARG} + 1",
            f"@{ARG}",
            "D=M+1",
            f"@{SP}",
            "M=D",
        ]
        new_lines.extend(nl)

        ## THAT = *(endFrame - 1)

        nl = [f"// {THAT_SYMBOL} = *(endFrame - 1)"]
        new_lines.extend(nl)

        nl = self.translate_derefer_endframe_diff(1)
        new_lines.extend(nl)

        nl = [
            f"@{THAT_SYMBOL}",
            "M=D",
        ]
        new_lines.extend(nl)

        ## THIS = *(endFrame - 2)

        nl = [f"// {THIS_SYMBOL} = *(endFrame - 2)"]
        new_lines.extend(nl)

        nl = self.translate_derefer_endframe_diff(2)
        new_lines.extend(nl)

        nl = [
            f"@{THIS_SYMBOL}",
            "M=D",
        ]
        new_lines.extend(nl)

        ## ARG = *(endFrame - 3)

        nl = [f"// {ARG} = *(endFrame - 3)"]
        new_lines.extend(nl)

        nl = self.translate_derefer_endframe_diff(3)
        new_lines.extend(nl)

        nl = [
            f"@{ARG}",
            "M=D",
        ]
        new_lines.extend(nl)  

        ## LCL = *(endFrame - 4)

        nl = [f"// {LCL} = *(endFrame - 4)"]
        new_lines.extend(nl)

        nl = self.translate_derefer_endframe_diff(4)
        new_lines.extend(nl)

        nl = [
            f"@{LCL}",
            "M=D",
        ]
        new_lines.extend(nl)

        nl = [
            f"@{RET_ADDR}",
            "A=M",
            "0;JMP",
        ]
        new_lines.extend(nl)

        return new_lines
    
    def translate_derefer_endframe_diff(self, val):
        """Sets D = *(endFrame - val)"""

        new_lines = [
            f"@{val}",
            "D=A",
            f"@{END_FRAME}",
            "A=M-D",
            "D=M",
        ]
        return new_lines

def main(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    print(f"Read {file_path}")

    head, tail = os.path.split(file_path)
    if not tail:
        raise ValueError

    assert tail.endswith(".vm")
    fn = tail.split(".vm")[0]

    vm_translator = VmTranslator(fn)
    lines_stripped = vm_translator.pre_process(lines)
    processed_lines = vm_translator.process(lines_stripped)

    out_name = f"{fn}.asm"
    out_path = os.path.join(head, out_name)
    with open(out_path, "w") as f:
        f.writelines("\n".join(processed_lines))

    print(f"Output written to {out_path}")
    print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")

    args = parser.parse_args()
    file_path = args.file_path
    main(file_path)
