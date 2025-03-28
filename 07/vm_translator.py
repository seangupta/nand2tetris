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
    def __init__(self, fn, no_bootstrap, call_counters=None):
        self.num_labels = 0
        self.fn = fn
        if call_counters is None:
            self.call_counters = {}
        else:
            self.call_counters = call_counters
        self.no_bootstrap = no_bootstrap

    @staticmethod
    def pre_process(lines):
        print("Stripping whitespace and comments")
        lines_stripped = []
        for line in lines:
            line = line.split("//")[0]
            line = line.strip()
            if line:
                # print(line)
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

        if not self.no_bootstrap:
            print("Generating bootstrap code")
            new_lines = self.generate_bootstrap_code()
            processed_lines.extend(new_lines)

        print("Generating main code")
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

        nl = [
                f"// RAM[{SP}] = D",
                f"@{SP}",
                "A=M",
                "M=D",
                f"// {SP}++",
                f"@{SP}",
                "M=M+1",
            ]
        new_lines.extend(nl)

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
        new_lines = [
            f"// VM: {op}",
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "A=A-1",  
            ]

        if op in [ADD, SUB, AND, OR]:
            if op == ADD:
                assembly_op = "+"
            elif op == SUB:
                assembly_op = "-"
            elif op == AND:
                assembly_op = "&"
            elif op == OR:
                assembly_op = "|"

            nl = [f"M=M{assembly_op}D"]
            
        elif op in [EQ, GT, LT, AND, OR]:
            if op == EQ:
                assembly_op = "-"
                comp = "JEQ"
            elif op == GT:
                assembly_op = "-"
                comp = "JGT"
            elif op == LT:
                assembly_op = "-"
                comp = "JLT"
            elif op == AND:
                assembly_op = "&"
                comp = "JNE"
            elif op == OR:
                assembly_op = "|"
                comp = "JNE"

            nl = [
                f"D=M{assembly_op}D",
                "M=-1",
                f"@TRUE{self.num_labels}",
                f"D;{comp}",
                "@SP",
                "A=M-1"
                "M=0",
                f"(TRUE{self.num_labels})",
            ]
            self.num_labels += 1

        else:
            raise ValueError(f"Unknown op {op}")

        new_lines.extend(nl)

        return new_lines

    def translate_unary_op(self, op):
        if op == NEG:
            assembly_op = "-"
        elif op == NOT:
            assembly_op = "!"
        else:
            raise ValueError(f"Unknown op {op}")

        new_lines = [
            f"// VM: {op}",
            "@SP",
            "A=M-1",
            f"M={assembly_op}M",
            ]
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

        new_lines = [f"// VM: call {function_name} {num_args}"]

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
        nl = [
            f"@{SP}",
            "D=M",
            "@5",
            "D=D-A",
            f"@{num_args}",
            "D=D-A",
            f"@{ARG}",
            "M=D",
        ]
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

        new_lines = ["// VM: return"]

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

def main(path, no_bootstrap=False):

    if os.path.isfile(path):
        with open(path, "r") as f:
            lines = f.readlines()
        print(f"Read {path}")

        head, tail = os.path.split(path)
        if not tail:
            raise ValueError

        assert tail.endswith(".vm")
        fn = tail.split(".vm")[0]
        out_path = os.path.join(head, f"{fn}.asm")

        vm_translator = VmTranslator(fn, no_bootstrap=no_bootstrap)
        lines_stripped = vm_translator.pre_process(lines)
        processed_lines = vm_translator.process(lines_stripped)

    elif os.path.isdir(path):
        processed_lines = []
        num_files_processed = 0
        call_counters = None
        for fn in os.listdir(path):
            if not fn.endswith(".vm"):
                continue
            
            full_path = os.path.join(path, fn)
            with open(full_path, "r") as f:
                lines = f.readlines()
            print(f"Read {full_path}")

            vm_translator = VmTranslator(fn, no_bootstrap=no_bootstrap or num_files_processed > 0,
                                         call_counters=call_counters)
            lines_stripped = vm_translator.pre_process(lines)
            processed_lines_this_file = vm_translator.process(lines_stripped)
            processed_lines.extend(processed_lines_this_file)

            num_files_processed += 1
            call_counters = vm_translator.call_counters

        if num_files_processed == 0:
            raise ValueError("No .vm files found")

        out_path = os.path.join(path, f"{os.path.split(path)[-1]}.asm")

    else:
        raise ValueError("Unknown path type")

    with open(out_path, "w") as f:
        f.writelines("\n".join(processed_lines))

    print(f"Output written to {out_path}")
    print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--no_bootstrap", action='store_true', default=False)
    args = parser.parse_args()
    main(args.path, no_bootstrap= args.no_bootstrap)
